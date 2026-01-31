@echo off
setlocal ENABLEDELAYEDEXPANSION

echo ===============================
echo  NUSUK SETUP (Python + deps)
echo ===============================
echo.

:: 1) Vérifier Python
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [INFO] Python non trouve - installation via winget...
    winget -v >nul 2>&1
    if %ERRORLEVEL% NEQ 0 (
        echo [ERREUR] winget n'est pas disponible sur ce Windows.
        echo Installe Python manuellement depuis https://www.python.org/downloads/windows/ puis relance ce script.
        pause
        exit /b 1
    )
    echo Installation de Python 3.12...
    winget install -e --id Python.Python.3.12 --source winget --accept-package-agreements --accept-source-agreements
    if %ERRORLEVEL% NEQ 0 (
        echo [ERREUR] Echec installation Python via winget.
        pause
        exit /b 1
    )
)

echo.
echo [OK] Python trouve :
python --version
echo.

:: 2) Créer venv .venv
if not exist ".venv" (
    echo Creation de l'environnement virtuel .venv ...
    python -m venv .venv
    if %ERRORLEVEL% NEQ 0 (
        echo [ERREUR] Echec creation venv.
        pause
        exit /b 1
    )
) else (
    echo [INFO] Environnement .venv deja present.
)

:: 3) Activer venv et installer requirements
echo.
echo Activation de .venv et installation des dependances...
call ".venv\Scripts\activate.bat"

:: Si requirements.txt existe, on l'utilise, sinon on installe les 3 paquets directement
if exist "requirements.txt" (
    pip install --upgrade pip
    pip install -r requirements.txt
) else (
    pip install --upgrade pip
    pip install selenium webdriver-manager python-dotenv
)

if %ERRORLEVEL% NEQ 0 (
    echo [ERREUR] Installation des dependances echouee.
    pause
    exit /b 1
)

echo.
echo ===============================
echo  INSTALLATION TERMINEE ✅
echo ===============================
echo Pour lancer le script :
echo   1. Double-cliquer sur run_nusuk.bat
echo      (ou dans ce terminal: 
echo          call .venv\Scripts\activate.bat
echo          python selenium_keepalive.py )
echo.
pause
endlocal
