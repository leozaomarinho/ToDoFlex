@echo off
REM ativa o ambiente virtual
call venv\Scripts\activate.bat

REM inicia o servidor FastAPI
uvicorn app.main:app --reload

REM mantem a janela aberta após o termino
pause