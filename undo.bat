@echo off
:: Checking for Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    pause
    exit /b
)

:: Running the script with current directory context
python "%~dp0undo.py"
pause