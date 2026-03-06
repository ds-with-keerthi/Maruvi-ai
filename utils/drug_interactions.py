import boto3
import json

bedrock = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)


def check_drug_interactions(medicine_list):

    if len(medicine_list) < 2:
        return []

    medicines = ", ".join(medicine_list)

    prompt = f"""
You are a medical safety assistant.

The following medicines are prescribed together:

{medicines}

Check if there are any known drug interactions or safety concerns.

Return ONLY JSON in this format:

[
  {{
    "medicine_pair": "",
    "risk": "",
    "recommendation": ""
  }}
]

If there are no interactions return:

[]
"""

    body = {
        "schemaVersion": "messages-v1",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"text": prompt}
                ]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 300,
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

    output_text = result["output"]["message"]["content"][0]["text"]

    try:
        return json.loads(output_text)
    except:
        return []