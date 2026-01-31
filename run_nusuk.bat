@echo off
setlocal
if not exist ".venv" (
    echo [ERREUR] .venv manquant. Lance d'abord install_nusuk_env.bat
    pause
    exit /b 1
)
call ".venv\Scripts\activate.bat"
python selenium_keepalive.py
pause
endlocal
