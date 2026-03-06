import re


def clean_prescription_text(text):

    text = text.lower()

    # remove common noise words
    noise_words = [
        "after food",
        "before food",
        "for 5 days",
        "for 3 days",
        "take rest",
        "drink water",
        "juice",
        "diet"
    ]

    for word in noise_words:
        text = text.replace(word, "")

    # remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()