def create_voice_summary(medicines, language="en"):

    if language == "hi":

        speech = "यह आपके प्रिस्क्रिप्शन की जानकारी है। "

        for med in medicines:

            name = med.get("medicine","")
            purpose = med.get("purpose","")
            freq = med.get("frequency","")

            speech += f"{name} का उपयोग {purpose} के लिए किया जाता है। "
            speech += f"इसे {freq} लें। "

    else:

        speech = "Here is the explanation of your prescription. "

        for med in medicines:

            name = med.get("medicine","")
            purpose = med.get("purpose","")
            freq = med.get("frequency","")

            speech += f"{name} is used for {purpose}. "
            speech += f"Take it {freq}. "

    return speech