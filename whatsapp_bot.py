from fastapi import FastAPI, Request, Response
from twilio.twiml.messaging_response import MessagingResponse

import requests
from requests.auth import HTTPBasicAuth
import os

from utils.textract_ocr import extract_text_from_image
from utils.bedrock_llm import explain_medicine
from utils.medicine_chat import answer_medicine_question
from utils.polly_tts import generate_speech
from utils.upload_audio import upload_audio
from utils.voice_summary import create_voice_summary
from utils.dynamodb_session import save_session, get_session
from utils.allergy_database import get_allergy_warning
from utils.buy_links import get_buy_links


app = FastAPI()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")


@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):

    try:

        form = await request.form()
        resp = MessagingResponse()

        user_number = form.get("From")
        incoming_text = form.get("Body", "").lower()
        num_media = int(form.get("NumMedia", 0))

        # -------------------------------
        # LANGUAGE DETECTION
        # -------------------------------

        language = "en"

        if "hindi" in incoming_text or "हिंदी" in incoming_text:
            language = "hi"

        # -------------------------------
        # CASE 1: PRESCRIPTION IMAGE
        # -------------------------------

        if num_media > 0:

            media_url = form.get("MediaUrl0")

            image_bytes = requests.get(
                media_url,
                auth=HTTPBasicAuth(
                    TWILIO_ACCOUNT_SID,
                    TWILIO_AUTH_TOKEN
                )
            ).content

            # OCR
            extracted_text = extract_text_from_image(image_bytes)

            # LLM extraction
            medicines = explain_medicine(extracted_text.strip())

            # print("LLM RAW OUTPUT:", medicines)
            # print("TYPE:", type(medicines))

            # Ensure medicines is always a list
            if isinstance(medicines, dict):
                medicines = medicines.get("medicines", [])

            if not isinstance(medicines, list):
                medicines = []

            # Inject allergy warnings
            for med in medicines:
                if isinstance(med, dict):
                    med["allergy_warning"] = get_allergy_warning(
                        med.get("medicine", "")
                    )

            # Save session
            save_session(user_number, medicines)

            # -------------------------------
            # SEND HEADER MESSAGE
            # -------------------------------

            # resp.message(
            #     "🩺 *Prescription Analysis Complete*\n"
            #     "Here are the medicines detected:"
            # )

            # -------------------------------
            # SEND EACH MEDICINE SEPARATELY
            # -------------------------------

            for med in medicines:
                links = get_buy_links(med.get("medicine", ""))

                msg = f"""💊 *{med.get('medicine','Unknown Medicine')}*

                        Purpose: {med.get('purpose','Use as prescribed')}
                        Dosage: {med.get('dosage','Follow doctor instructions')}
                        Frequency: {med.get('frequency','Take as directed')}
                        Precautions: {med.get('precautions','Consult doctor if unsure')}
                        ⚠ Allergy: {med.get('allergy_warning','Consult doctor if allergic')}

                        🛒 *Buy Online*

                        1mg:
                    {links['1mg']}

                        PharmEasy:
                        {links['pharmeasy']}

                        Netmeds:
                        {links['netmeds']}
                        """

                resp.message(msg)

            # -------------------------------
            # SAFETY ADVICE MESSAGE
            # -------------------------------

            resp.message(
                """⚠ *General Safety Advice*

• Always follow the dosage prescribed by your doctor.
• Complete the full course for antibiotics.
• Do not self-medicate or stop medicines early.
• Consult a doctor if symptoms worsen.
"""
            )

            # -------------------------------
            # VOICE EXPLANATION
            # -------------------------------

            speech_text = create_voice_summary(medicines, language)

            audio_bytes = generate_speech(speech_text, language)

            audio_url = upload_audio(audio_bytes)

            voice_msg = resp.message("🔊 Voice explanation")
            voice_msg.media(audio_url)

        # -------------------------------
        # CASE 2: FOLLOW-UP QUESTIONS
        # -------------------------------

        else:

            medicines = get_session(user_number)

            if medicines:

                answer = answer_medicine_question(
                    incoming_text,
                    medicines
                )

                resp.message(answer)

            else:

                resp.message(
                    "📷 Please send a prescription image first so I can analyze your medicines."
                )

        return Response(
            content=str(resp),
            media_type="application/xml"
        )

    except Exception as e:

        print("ERROR:", str(e))

        resp = MessagingResponse()
        resp.message(
            "⚠️ Something went wrong while processing the request."
        )

        return Response(
            content=str(resp),
            media_type="application/xml"
        )