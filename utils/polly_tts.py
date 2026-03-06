import boto3

polly = boto3.client("polly", region_name="ap-south-1")


def generate_speech(text, language="en"):

    if language == "hi":
        voice = "Aditi"
    else:
        voice = "Joanna"

    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId=voice
    )

    return response["AudioStream"].read()