@echo off
REM DyslexiaCheck - Startup Script for Windows

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                     DYSLEXIACHECK                            ║
echo ║         Early Detection ^& Support Platform                   ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    py -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
echo.

REM Install requirements
echo Installing/checking dependencies...
pip install -r requirements.txt --upgrade pip setuptools
if errorlevel 1 (
    echo.
    echo ⚠️  Dependency installation encountered an issue.
    echo Attempting to continue anyway...
    echo.
)

REM Start the application
echo Starting DyslexiaCheck application...
echo The application will be available at: http://localhost:5000
echo.
python run.py

pause
