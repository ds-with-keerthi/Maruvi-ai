import boto3
import json
import re

# Bedrock runtime client
bedrock = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)


def explain_medicine(prescription_text):
    """
    Sends Textract OCR prescription text to Amazon Nova Lite
    and returns structured JSON with medicine explanation.
    """

    prompt = f"""
    You are an AI medical assistant helping patients understand prescriptions.

    The text below was extracted from a doctor's handwritten prescription using OCR.
    OCR text may contain spelling errors, broken words, or formatting issues.

    Your tasks:

    1. Identify ONLY real medicines mentioned in the prescription.
    2. Correct obvious OCR spelling mistakes in medicine names.
    3. Extract dosage and frequency if available.
    4. Explain what the medicine is typically used for.
    5. Provide simple safety precautions for the patient.
    6. Provide allergy warnings related to that medicine.

    ------------------------------------
    MEDICINE DETECTION RULES
    ------------------------------------

    Medicine names in prescriptions often appear with prefixes such as:

    Tab, Tablet, Cap, Capsule, Syp, Syrup, Inj, Injection, Drop, Oint, Cream.

    Examples:

    Tab Paracetmol → Paracetamol  
    Syp Ambrodic → Ambrodic Syrup  
    Cap Amoxilin → Amoxicillin Capsule

    If the medicine name is abbreviated (example: OFM, PCM, AZM), infer the likely full medicine name when possible.

    Return the medicine name in a clean readable form.

    Example:
    "Syp OFM" → "OFM Syrup"

    ------------------------------------
    IGNORE NON-MEDICINE ITEMS
    ------------------------------------

    Ignore items that are NOT medicines such as:

    • juice  
    • water  
    • diet advice  
    • ORS unless clearly written as medicine  
    • general instructions like "rest well"  

    ------------------------------------
    DOSAGE PATTERN RULES
    ------------------------------------

    Interpret common doctor shorthand:

    1-0-1 = morning and evening  
    1-1-1 = morning, afternoon, evening  
    0-0-1 = night only  

    Convert frequency into ONLY one of these standard formats:

    once daily  
    twice daily  
    three times daily  
    every 4 hours  
    every 6 hours  

    If dosage or frequency cannot be clearly determined,
    provide a reasonable patient-safe statement instead of leaving it empty.

    Examples:

    dosage → "Use as prescribed by the doctor"  
    frequency → "Take as directed by the doctor"

    ------------------------------------
    PATIENT SAFETY RULES
    ------------------------------------

    Precautions should be simple and safe such as:

    • Do not exceed recommended dose  
    • Take after food  
    • Complete full course if antibiotic  
    • Consult doctor if symptoms persist  

    ------------------------------------
    ALLERGY WARNING RULES
    ------------------------------------

    For each medicine include a short allergy warning.

    Examples:

    Paracetamol → Avoid if allergic to paracetamol. Seek medical help if rash or swelling occurs.

    Antibiotics → Avoid if allergic to similar antibiotics.

    Antihistamines → May cause drowsiness. Avoid if allergic to antihistamines.

    If allergy information is uncertain, use:

    "Consult your doctor if you have known medicine allergies."

    ------------------------------------
    OUTPUT FORMAT RULES
    ------------------------------------

    Return ONLY valid JSON.

    Do NOT include explanations before or after the JSON.
    Do NOT include markdown formatting.

    JSON format:

    [
    {{
        "medicine": "",
        "purpose": "",
        "dosage": "",
        "frequency": "",
        "precautions": "",
        "allergy_warning": "",
        "notes": ""
    }}
    ]

    ------------------------------------
    EXAMPLE
    ------------------------------------

    Input:

    Tab Amoxilin 250  
    1-1-1  
    5 days

    Output:

    [
    {{
        "medicine": "Amoxicillin 250 mg tablet",
        "purpose": "Antibiotic used to treat bacterial infections",
        "dosage": "250 mg tablet",
        "frequency": "three times daily",
        "precautions": "Complete the full course even if symptoms improve",
        "allergy_warning": "Avoid if allergic to penicillin or related antibiotics",
        "notes": "Take for 5 days"
    }}
    ]

    ------------------------------------

    Prescription text:
    {prescription_text}
    """
    
    response = bedrock.invoke_model(
        modelId="amazon.nova-lite-v1:0",
        body=json.dumps({
            "messages": [
                {"role": "user", "content": [{"text": prompt}]}
            ]
        })
    )

    response_body = json.loads(response["body"].read())

    # Extract the LLM text output
    llm_text = response_body["output"]["message"]["content"][0]["text"]

    print("LLM TEXT:", llm_text)

    # Convert JSON string → Python list
    try:
        medicines = json.loads(llm_text)
    except Exception as e:
        print("JSON parsing error:", e)
        medicines = []

    return medicines