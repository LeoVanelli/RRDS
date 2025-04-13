import csv
import logging
import re
import pandas as pd
import os
from typing import List, Dict
from config.settings import Settings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def ensure_directories(settings: Settings) -> None:
    try:
        os.makedirs(os.path.dirname(settings.INPUT_CSV), exist_ok=True)
        os.makedirs(os.path.dirname(settings.OUTPUT_EXCEL), exist_ok=True)
    except Exception as e:
        logging.error(f"Erro ao criar diretórios: {e}")


def read_registros_csv(filename: str) -> List[str]:
    registros = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if 'cod_imovel' in row:
                    registros.append(row['cod_imovel'])
        logging.info(f"Lidos {len(registros)} registros do CSV")
        return registros
    except Exception as e:
        logging.error(f"Erro ao ler CSV {filename}: {e}")
        return []


def save_to_excel(data: List[Dict], filename: str) -> None:
    try:
        output_dir = os.path.dirname(filename)
        base_name = "resultado_registros_incra_batch_"
        extension = ".xlsx"

        max_number = 0
        if os.path.exists(output_dir):
            for existing_file in os.listdir(output_dir):
                match = re.match(rf"{base_name}(\d+){extension}", existing_file)
                if match:
                    number = int(match.group(1))
                    max_number = max(max_number, number)

        new_filename = os.path.join(output_dir, f"{base_name}{max_number + 1}{extension}")

        df = pd.DataFrame(data, columns=['cod_imovel', 'nomeImovel', 'nomeProprietario'])
        df.to_excel(new_filename, index=False)
        logging.info(f"Resultados salvos em {new_filename}")
    except Exception as e:
        logging.error(f"Erro ao salvar Excel: {e}")