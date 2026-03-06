import streamlit as st
import pandas as pd

from utils.textract_ocr import extract_text_from_image
from utils.bedrock_llm import explain_medicine
from utils.polly_tts import generate_speech
from utils.s3_storage import upload_to_s3
from utils.generate_reminder import generate_reminder_schedule
from utils.drug_interactions import check_drug_interactions
from utils.ocr_cleaner import clean_prescription_text
from utils.translator import translate_text

import boto3
import json

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")


def translate_text(text, language):

    if language == "English":
        return text

    prompt = f"""
Translate the following medical explanation into {language}.
Keep the meaning simple and clear for patients.

Text:
{text}
"""

    body = {
        "schemaVersion": "messages-v1",
        "messages": [
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 500,
            "temperature": 0.1
        }
    }

    response = bedrock.invoke_model(
        modelId="amazon.nova-lite-v1:0",
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(response["body"].read())

    return result["output"]["message"]["content"][0]["text"]

st.set_page_config(page_title="Maruvi AI", layout="wide")

st.title("Maruvi AI")
st.subheader("Know the medicine you take")

uploaded_file = st.file_uploader(
    "Upload Prescription Image",
    type=["jpg", "jpeg", "png"]
)

def create_voice_summary(medicines):

    speech_text = ""

    for med in medicines:

        name = med.get("medicine","")
        purpose = med.get("purpose","")
        freq = med.get("frequency","")

        speech_text += f"{name} is used for {purpose}. Take it {freq}. "

    return speech_text

if uploaded_file:

    image_bytes = uploaded_file.read()

    # Upload image to S3
    upload_to_s3(image_bytes, uploaded_file.name)

    # Show image
    st.image(
        uploaded_file,
        caption="Uploaded Prescription",
        use_column_width=True
    )

    # TEXTRACT OCR
    with st.spinner("Reading prescription using AWS Textract..."):
        raw_text = extract_text_from_image(image_bytes)
        extracted_text = clean_prescription_text(raw_text)

    st.success("Prescription text extracted")

    st.text_area(
        "Extracted Text",
        extracted_text,
        height=200
    )

    # LLM ANALYSIS
    with st.spinner("Analyzing medicines using AWS Bedrock..."):

        structured_output = explain_medicine(extracted_text)

        # Extract medicine names
        medicine_names = [
            med.get("medicine", "")
            for med in structured_output
            if med.get("medicine")]
        
        # Detect interactions
        interactions = check_drug_interactions(medicine_names)

        # Handle parsing failure
        if isinstance(structured_output, dict) and "raw_output" in structured_output:

            st.error("Could not parse structured medicine output")

            st.markdown("### Raw Model Output")
            st.write(structured_output["raw_output"])

        else:

            for medicine in structured_output:

                # Generate reminder schedule
                frequency = medicine.get("frequency", "Not specified")

                try:
                    reminders = generate_reminder_schedule(frequency)
                    medicine["reminder_schedule"] = ", ".join(reminders)

                except Exception:
                    medicine["reminder_schedule"] = "Could not generate"

            st.success("Medicine explanation generated")

            # Convert to dataframe
            df = pd.DataFrame(structured_output)

            st.markdown("### Extracted Medicines")

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )
        
            
            if interactions:

                st.markdown("### ⚠ Potential Drug Interactions")
                interaction_df = pd.DataFrame(interactions)
                st.dataframe(
                        interaction_df,
                        use_container_width=True,
                        hide_index=True
                    )

            else:
                st.success("No major drug interactions detected")

            # Optional voice explanation
            language = st.selectbox("Select Explanation Language",["English", "Tamil", "Hindi"])
            voice_map = {"English": "Joanna", "Tamil": "Aditi", "Hindi": "Aditi"}
            
            if st.button("🔊 Listen to Medicine Explanation"):

                voice = voice_map[language]

                speech_text = create_voice_summary(structured_output)
                speech_text = create_voice_summary(structured_output)

                translated_text = translate_text(speech_text, language)

                audio_bytes = generate_speech(translated_text, voice)

                st.audio(audio_bytes, format="audio/mp3")
    st.warning(
        "⚠ This tool provides informational guidance only. Always consult a doctor before taking medication."
    )