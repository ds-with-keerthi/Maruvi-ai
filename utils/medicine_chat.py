import boto3
import json

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def answer_medicine_question(question, medicines):

    context = json.dumps(medicines)

    prompt = f"""
You are a medical assistant helping patients understand their prescription.

Prescription medicines:
{context}

Patient question:
{question}

Answer clearly and simply.
"""

    body = {
        "schemaVersion": "messages-v1",
        "messages": [
            {"role": "user", "content": [{"text": prompt}]}
        ],
        "inferenceConfig": {
            "maxTokens": 300,
            "temperature": 0.2
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