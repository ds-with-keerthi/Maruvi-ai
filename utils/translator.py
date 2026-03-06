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