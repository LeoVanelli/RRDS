import logging
import random
import time
import os
import sys
from typing import List, Dict
from patchright.sync_api import sync_playwright
from config.settings import Settings
from src.auth import perform_login, accept_cookies
from src.file_handler import read_registros_csv, save_to_excel, ensure_directories
from src.scraper import extract_fields

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def run_scraper(settings: Settings) -> None:
    ensure_directories(settings)

    registros = read_registros_csv(settings.INPUT_CSV)
    if not registros:
        logging.error("Nenhum registro encontrado. Encerrando.")
        return

    results: List[Dict] = []

    with sync_playwright() as p:
        browser = None
        try:
            if getattr(sys, 'frozen', False):
                base_path = sys._MEIPASS
                chromium_path = os.path.join(base_path, "patchright", "browser", "chrome-win", "chrome.exe")
            else:
                chromium_path = r"C:\Users\%USERPROFILE%\AppData\Local\ms-playwright\chromium-1161\chrome-win\chrome.exe"

            if not os.path.exists(chromium_path):
                logging.error(f"Chromium não encontrado em: {chromium_path}")
                raise FileNotFoundError(f"Chromium não encontrado em: {chromium_path}")

            browser = p.chromium.launch(
                headless=False,
                executable_path=chromium_path
            )
            logging.info(f"Navegador iniciado com Chromium em: {chromium_path}")

            context = browser.new_context(
                user_agent=settings.USER_AGENT,
                viewport=settings.VIEWPORT
            )
            page = context.new_page()

            if not perform_login(page, settings):
                logging.error("Encerrando devido a falha no login")
                return

            time.sleep(random.uniform(2, 4))

            if not accept_cookies(page):
                logging.error("Falha ao aceitar cookies.")

            for i in range(0, len(registros), settings.BATCH_SIZE):
                batch = registros[i:i + settings.BATCH_SIZE]
                logging.info(f"Processando lote {i//settings.BATCH_SIZE + 1} ({len(batch)} registros)")

                for cod_imovel in batch:
                    try:
                        url = settings.BASE_URL.format(cod_imovel)
                        logging.info(f"Acessando {url}")
                        page.goto(url, timeout=60000)
                        time.sleep(random.uniform(2, 4))

                        data = extract_fields(page, cod_imovel, settings)
                        results.append(data)
                        logging.info(f"Extraído: {data}")

                        time.sleep(random.uniform(1, 3))
                    except Exception as e:
                        logging.error(f"Erro ao processar {cod_imovel}: {e}")
                        results.append({
                            "cod_imovel": cod_imovel,
                            "nomeImovel": "Erro",
                            "nomeProprietario": "Erro"
                        })

                save_to_excel(results, settings.OUTPUT_EXCEL)

                if i + settings.BATCH_SIZE < len(registros):
                    logging.info(f"Pausando por {settings.BATCH_PAUSE} segundos...")
                    time.sleep(settings.BATCH_PAUSE)

            logging.info("Processamento concluído")
        except Exception as e:
            logging.error(f"Erro geral: {e}")
            raise
        finally:
            save_to_excel(results, settings.OUTPUT_EXCEL)
            if browser:
                browser.close()
                logging.info("Navegador fechado com sucesso.")