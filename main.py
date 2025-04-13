import logging
from config.settings import Settings
from src.api import run_scraper

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    try:
        settings = Settings()
        logging.info("Iniciando o script para web scrapping do Registro Rural...")

        run_scraper(settings)

        logging.info("Processamento concluído com sucesso.")
        print("Script concluído com sucesso!")
        print("Resultados salvos em: batch\\result\\nome_resultado_batch_X.xlsx")

    except Exception as e:
        logging.error(f"Erro durante a execução do script: {e}")
        print(f"Erro: {e}")

    finally:
        input("Pressione Enter para sair...")