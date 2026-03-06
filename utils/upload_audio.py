import boto3
import uuid

s3 = boto3.client("s3")

BUCKET_NAME = "maruvi-prescriptions-aiforbharat"

def upload_audio(audio_bytes):

    file_name = f"audio/{uuid.uuid4()}.mp3"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=audio_bytes,
        ContentType="audio/mpeg"
    )

    url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{file_name}"

    return url