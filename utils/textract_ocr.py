import boto3

textract = boto3.client("textract", region_name="ap-south-1")


def extract_text_from_image(image_bytes):

    response = textract.detect_document_text(
        Document={"Bytes": image_bytes}
    )

    if "Blocks" not in response:
        return ""

    extracted_text = ""

    for block in response["Blocks"]:
        if block["BlockType"] == "LINE":
            extracted_text += block["Text"] + "\n"

    return extracted_text