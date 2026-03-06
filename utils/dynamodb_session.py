import boto3
import json

dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")

table = dynamodb.Table("maruvi_sessions")


def save_session(user_id, medicines):

    table.put_item(
        Item={
            "user_id": user_id,
            "medicines": json.dumps(medicines)
        }
    )


def get_session(user_id):

    response = table.get_item(
        Key={"user_id": user_id}
    )

    if "Item" in response:

        return json.loads(response["Item"]["medicines"])

    return None