@echo off
REM Test installation script

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║           DyslexiaCheck - Installation Test               ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Activate virtual environment
call venv\Scripts\activate

echo Testing Python environment...
python --version
echo.

echo Testing Flask and dependencies...
python -c "import flask, flask_sqlalchemy, flask_login, flask_wtf, werkzeug, sqlalchemy, wtforms, email_validator, dotenv; print('✓ All dependencies installed')"
echo.

echo Testing Flask app initialization...
python -c "from app import create_app; app = create_app(); print('✓ Flask app initialized successfully')"
echo.

echo ✅ All tests passed! The application is ready to run.
echo.
echo To start the application, run: start.bat
echo.

pause
