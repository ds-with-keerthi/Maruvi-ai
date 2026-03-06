allergy_db = {
    "PARACETAMOL": "Avoid if allergic to paracetamol. Seek medical help if rash or swelling occurs.",
    "FEPANIC": "Avoid if allergic to antihistamines. May cause mild drowsiness.",
    "RESCOLD": "Avoid if allergic to antihistamines or decongestants.",
    "AMBRODIC": "Consult doctor if allergic to ambroxol or similar cough medicines.",
    "OFM": "Avoid if allergic to cephalosporin antibiotics.",
    "VOMIKIND": "Avoid if allergic to ondansetron or related medicines.",
    "ORS": "Generally safe but consult doctor if electrolyte imbalance conditions exist."
}


def get_allergy_warning(medicine_name):

    name = medicine_name.upper()

    for key in allergy_db:
        if key in name:
            return allergy_db[key]

    return "Consult your doctor if you have known medicine allergies."