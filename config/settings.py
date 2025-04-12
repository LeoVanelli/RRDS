from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Settings:
    LOGIN_URL: str = (
        "https://www.registrorural.com.br/accounts/login/?next=/?gad_source=1&gclid"
        "=Cj0KCQjwnui_BhDlARIsAEo9Gutr4G6r-oo7Vd346xicCaoDoqkTLzuzDysXCrubfYk82nsf-aFAsZAaAs0YEALw_wcB"
    )
    BASE_URL: str = "https://www.registrorural.com.br/car/item/{}/"
    EMAIL: str = "seuemail"
    PASSWORD: str = "suasenha"
    INPUT_CSV: str = "batch/queue/registros_incra.csv"
    OUTPUT_EXCEL: str = "batch/result/resultados_registroRural.xlsx"
    BATCH_SIZE: int = 250
    BATCH_PAUSE: int = 120
    USER_AGENT: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    VIEWPORT: Dict[str, int] = field(default_factory=lambda: {
        "width": 1280,
        "height": 720
    })

    LOGIN_EMAIL_SELECTOR: str = "#id_login"
    LOGIN_PASSWORD_SELECTOR: str = "#id_password"
    LOGIN_SUBMIT_SELECTOR: str = "button.btn.btn-primary.w-100.mt-2.primaryAction"

    NOME_IMOVEL_SELECTOR: str = (
        "#containerCarDetails div.card.mb-3.shadow-lg div.card-body h1.card-title.fs-5"
    )
    CADASTRANTE_CARD_SELECTOR: str = "p.card-text"
    CADASTRANTE_SELECTOR: str = "small.text-muted"
