@echo off
ECHO Iniciando configuracao e execucao do projeto RRDS - Registro Rural Data Scrapping...

:: Verificar se o Python esta instalado
ECHO Verificando Python...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO Erro: Python nao encontrado. Instale o Python 3.8+ e tente novamente.
    pause
    exit /b 1
)
ECHO Python encontrado.

:: Definir nome do ambiente virtual
SET VENV_DIR=venv

:: Criar ambiente virtual se nao existir
IF NOT EXIST %VENV_DIR% (
    ECHO Criando ambiente virtual...
    python -m venv %VENV_DIR%
    IF %ERRORLEVEL% NEQ 0 (
        ECHO Erro ao criar ambiente virtual.
        pause
        exit /b 1
    )
) ELSE (
    ECHO Ambiente virtual ja existe.
)

:: Ativar ambiente virtual
ECHO Ativando ambiente virtual...
CALL %VENV_DIR%\Scripts\activate.bat
IF %ERRORLEVEL% NEQ 0 (
    ECHO Erro ao ativar ambiente virtual.
    pause
    exit /b 1
)

:: Instalar dependencias
ECHO Instalando dependencias...
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    ECHO Erro ao instalar dependencias.
    pause
    exit /b 1
)
ECHO Dependencias instaladas.

:: Executar main.py
ECHO Executando main.py...
python main.py
IF %ERRORLEVEL% NEQ 0 (
    ECHO Erro ao executar main.py.
    pause
    exit /b 1
)
ECHO Execucao concluida.

:: Desativar ambiente virtual
ECHO Desativando ambiente virtual...
CALL %VENV_DIR%\Scripts\deactivate.bat

ECHO Processo finalizado.
pause