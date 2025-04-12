from config.settings import Settings
from src.api import run_scraper

if __name__ == "__main__":
    settings = Settings()
    run_scraper(settings)