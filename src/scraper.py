import logging
import random
import time
from typing import Dict
from patchright.sync_api import Page
from config.settings import Settings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def simulate_human_behavior(page: Page) -> None:
    try:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
        time.sleep(random.uniform(1, 3))
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(random.uniform(1, 2))
        page.mouse.move(random.randint(100, 800), random.randint(100, 600))
        time.sleep(random.uniform(0.5, 1))
    except Exception as e:
        logging.error(f"Erro ao simular comportamento: {e}")


def extract_fields(page: Page, cod_imovel: str, settings: Settings) -> Dict[str, str]:
    try:
        simulate_human_behavior(page)

        locator = page.locator(settings.NOME_IMOVEL_SELECTOR)
        locator.wait_for(timeout=5000)
        nome_imovel = locator.inner_text().strip()

        cadastrante_locator = page.locator("p.card-text:has(small.text-muted:has-text('Cadastrante'))")
        cadastrante_locator.wait_for(timeout=5000)

        nome_proprietario = cadastrante_locator.inner_text().split("\n")[0].strip() if cadastrante_locator else "Cadastrante não encontrado."

        return {
            "cod_imovel": cod_imovel,
            "nomeImovel": nome_imovel,
            "nomeProprietario": nome_proprietario
        }
    except Exception as e:
        logging.error(f"Erro ao extrair campos para {cod_imovel}: {e}")
        return {
            "cod_imovel": cod_imovel,
            "nomeImovel": "Erro",
            "nomeProprietario": "Erro"
        }
