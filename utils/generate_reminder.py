def generate_reminder_schedule(frequency):

    if not frequency:
        return ["Take only when needed"]

    frequency = frequency.lower()

    # twice daily
    if "twice" in frequency or "2" in frequency or "1-0-1" in frequency:
        return ["08:00 AM", "08:00 PM"]

    # three times daily
    elif "three" in frequency or "thrice" in frequency or "1-1-1" in frequency:
        return ["08:00 AM", "02:00 PM", "08:00 PM"]

    # once daily
    elif "once" in frequency or "1-0-0" in frequency:
        return ["08:00 AM"]

    # every 4 hours
    elif "4 hours" in frequency:
        return ["08:00 AM", "12:00 PM", "04:00 PM", "08:00 PM"]

    # every 6 hours
    elif "6 hours" in frequency:
        return ["06:00 AM", "12:00 PM", "06:00 PM", "12:00 AM"]

    else:
        return ["Consult doctor for schedule"]