import yaml
import pandas as pd
import os


def load_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def load_plates_from_excel(excel_path):
    if os.path.exists(excel_path):
        df = pd.read_excel(excel_path)
        placas = (
            df['Placa']
            .astype(str)
            .str.upper()
            .tolist()
        )
        return placas
    else:
        print(
            f"❌ Excel file not found / No se encontró el archivo Excel: "
            f"{excel_path}"
        )
        return []


def check_plate(detected_plate, valid_list):
    detected_plate = detected_plate.replace(" ", "").upper()
    return detected_plate in valid_list
