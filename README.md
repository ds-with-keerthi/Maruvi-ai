# Maruvi — AI Prescription Safety Assistant

Maruvi is an AI-powered prescription safety companion designed to help people understand the medicines they consume.

Users upload a prescription image, and Maruvi explains each medicine in simple language, shows active ingredients, safety precautions, dosage schedule, and generates reminders with multilingual voice support.

Tagline: *Know the medicine you take.*

---

## Problem Statement

Many people struggle to read prescriptions and understand medication instructions. This leads to missed doses, unsafe usage, and preventable health risks — especially among elderly and low-literacy populations in Bharat.

Maruvi bridges the gap between prescriptions and understanding.

---

## Solution Overview

Maruvi uses AI to:

- Extract text from prescription images
- Explain medicines in plain language
- Show active chemical ingredients
- Provide safety notes and precautions
- Generate smart reminder schedules
- Deliver multilingual voice guidance
- Operate as a WhatsApp / Telegram chatbot

The system is built using a serverless AWS architecture for scalability and affordability.

---

## Architecture Summary

User → Chatbot → API Gateway → AWS Lambda  
→ Textract (OCR) → Bedrock (AI reasoning) → Polly (Voice)  
→ DynamoDB + S3 storage

---

## Technologies Used

- Amazon Textract
- Amazon Bedrock
- AWS Polly
- AWS Lambda
- API Gateway
- DynamoDB
- S3 Storage
- Telegram / WhatsApp Bot API
- Python (Boto3 SDK)

---

## Key Features

- Prescription image scanning
- Plain-language medicine explanation
- Active ingredient transparency
- Safety notes & precautions
- AI-generated reminders
- Voice guidance in regional languages
- Caregiver-friendly design

---

## Future Scope

- Drug interaction safety alerts
- Offline rural deployment
- Government healthcare integration
- Pharmacy verification system
- AI-powered medicine authenticity checks

---

## Disclaimer

Maruvi provides educational guidance only and does not replace professional medical advice. Users should always follow instructions from licensed healthcare providers.

---

## Team

Team DSK  
AI for Bharat Hackathon Submission
