def read_plate_text(reader, image):
    results = reader.readtext(image)
    if results:
        return " ".join([r[1] for r in results])
    return ""


def extract_valid_plates(text):
    import re
    text = text.upper().replace(" ", "")
    patterns = [
        r'[A-Z]{2}[0-9]{4}',     # Placa estándar (ej: AB1234)
        r'M[0-9]{4}',            # Moto
        r'T[0-9]{5}',            # Taxi
        r'C[A-Z]{2}[0-9]{4}',    # Comercial
        r'D[0-9]{4}',            # Diplomática
        r'G[0-9]{4}',            # Gubernamental
        r'[0-9]{6,}'             # Números largos (sin letras) - nuevo
    ]
    found = set()
    for pattern in patterns:
        matches = re.findall(pattern, text)
        found.update(matches)
    return list(found)
