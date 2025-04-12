import logging
import random
from typing import Optional
from patchright.sync_api import Page
from config.settings import Settings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def accept_cookies(page: Page) -> bool:
    try:
        cookie_selectors = [
            "#adopt-accept-all-button",
            "button:contains('Aceitar')",
            "button:contains('Concordar')",
            "button:contains('OK')",
            ".cookie-accept",
            "#accept-cookies",
            "[id*='cookie'] button",
            "[class*='cookie'] button",
        ]
        for selector in cookie_selectors:
            cookie_button = page.query_selector(selector)
            if cookie_button:
                logging.info(f"Pop-up de cookies detectado. Clicando em: {selector}")
                cookie_button.click()
                page.wait_for_timeout(random.randint(1000, 2000))
                return True
        logging.info("Nenhum pop-up de cookies encontrado")
        return True
    except Exception as e:
        logging.error(f"Erro ao aceitar cookies: {e}")
        return False


def perform_login(page: Page, settings: Settings) -> bool:
    try:
        logging.info(f"Acessando página de login: {settings.LOGIN_URL}")
        page.goto(settings.LOGIN_URL, timeout=60000)
        page.wait_for_timeout(random.randint(2000, 4000))
        page.fill(settings.LOGIN_EMAIL_SELECTOR, settings.EMAIL)
        page.fill(settings.LOGIN_PASSWORD_SELECTOR, settings.PASSWORD)
        page.click(settings.LOGIN_SUBMIT_SELECTOR)
        page.wait_for_timeout(random.randint(3000, 5000))

        if page.url != settings.LOGIN_URL:
            logging.info("Login bem-sucedido")
            return True
        logging.error("Falha no login")
        return False
    except Exception as e:
        logging.error(f"Erro no login: {e}")
        return False