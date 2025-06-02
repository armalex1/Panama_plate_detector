def read_plate_text(reader, image):
    results = reader.readtext(image)
    if results:
        return "".join([r[1] for r in results])
    return ""


def extract_valid_plate(text):
    import re
    text = text.upper().replace(" ", "")
    patterns = [
        r'\b[A-Z]{2}[0-9]{4}\b',     # Particular
        r'\bM[0-9]{4}\b',            # Moto
        r'\bT[0-9]{5}\b',            # Taxi
        r'\bC[A-Z]{2}[0-9]{4}\b',    # Comercial
        r'\bD[0-9]{4}\b',            # Diplomática
        r'\bG[0-9]{4}\b',            # Gubernamental
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(0)
    return ""
