# Maruvi — AI Prescription Safety Assistant

Maruvi is an AI-powered prescription safety companion that helps people understand the medicines they consume.

Users simply upload a prescription image via WhatsApp, and Maruvi explains the medicines in simple language, provides safety precautions, generates reminder schedules, and even delivers multilingual voice guidance.

Maruvi — சாப்பிடும் மருந்தை அறி
"Know the medicine you take."

## PROBLEM STATEMENT:
Millions of patients struggle to understand prescriptions due to:

1. Complex medical terminology
2. Poor handwriting in prescriptions
3. Lack of medical literacy
4. Language barriers

This often results in:
- Missed doses
- Unsafe medicine combinations
- Medication misuse
- Preventable health complications

This issue is especially critical among:
1. Elderly patients
2. Rural populations
3. Low-literacy communities
4. Patients dependent on caregivers

Maruvi bridges the gap between prescriptions and understanding.

## SOLUTION:
Maruvi converts complex prescriptions into clear, understandable guidance for patients.

Using AI and AWS services, Maruvi can:
1. Extract text from prescription images
2. Identify medicines using AI
3. Explain medicines in simple language
4. Provide dosage and safety and allergy instructions
5. Deliver multilingual voice explanations
6. Shows online Buying options

Users interact with Maruvi through familiar messaging platforms such as WhatsApp.

## SYSTEM ARCHITECTURE:
User (WhatsApp / Telegram)
- FastAPI Backend (EC2)
- Amazon Textract (OCR extraction)
- Amazon Bedrock Nova (AI medicine understanding)
- Safety Intelligence Layer (allergy + precautions + reminders)
- Amazon Polly (voice explanation)
- DynamoDB (session memory)
- Amazon S3 (audio storage)
- Response returned to user via WhatsApp

## TECHNOLOGIES USED:
AI & ML
- Amazon Bedrock (Nova Models)
- Amazon Textract

Voice & Language
- AWS Polly (Multilingual Speech)

Cloud Infrastructure
- Amazon EC2
- DynamoDB
- Amazon S3

Backend
- FastAPI
- Python (Boto3 SDK)

Messaging Interface
- Twilio WhatsApp API

## EXAMPLE:
User sends prescription image on WhatsApp.

Maruvi responds:
💊 Vomikind Syrup
Purpose: Used to treat vomiting
Dosage: 5ml
Frequency: as needed
Precautions: Do not exceed recommended dose. Use as directed by the doctor. Take 30 minutes before feeding.
⚠ Allergy: Avoid if allergic to ondansetron or related medicines.

🛒 Buy Online
1mg:https://www.1mg.com/search/all?name=Vomikind%20Syrup
PharmEasy:https://pharmeasy.in/search/all?name=Vomikind%20Syrup
Netmeds:https://www.netmeds.com/catalogsearch/result?q=Vomikind%20Syrup

⚠ General Safety Advice
* Always follow the dosage prescribed by your doctor.
* Complete the full course for antibiotics.
* Do not self-medicate or stop medicines early.
* Consult a doctor if symptoms worsen.

Voice explanation is also sent via audio.

## INSTALLATION:
Clone the repository:
git clone https://github.com/ds-with-keerthi/Maruvi-ai.git
cd Maruvi-ai

Create virtual environment:
python -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Configure AWS credentials:
aws configure
Running the Application

Start the FastAPI server:
uvicorn whatsapp_bot:app --host 0.0.0.0 --port 8000

The API will be available at:
http://localhost:8000

## FUTURE SCOPE:
Maruvi can evolve into a complete AI healthcare assistant with features such as:
- Drug interaction safety alerts
- Caregiver monitoring dashboard
- Offline deployment for rural healthcare
- Government healthcare integration
- AI-based counterfeit medicine detection
- Personalized medication adherence analytics

## DISCLAIMER:
Maruvi provides educational guidance only and does not replace professional medical advice.
Users must always follow instructions from licensed healthcare providers.

## TEAM:
Team DSK
AI for Bharat Hackathon Submission

### Maruvi — Making medicine understanding simple for everyone.
