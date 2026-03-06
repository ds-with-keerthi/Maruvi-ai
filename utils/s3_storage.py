import boto3

s3 = boto3.client("s3", region_name="ap-south-1")

BUCKET_NAME = "maruvi-prescriptions-aiforbharat"

def upload_to_s3(file_bytes, filename):
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=file_bytes
    )