@echo off
echo Starting Hotel Agreement Form Generator...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Error: Virtual environment not found! >> service.log
    echo Please run 'python setup.py' first to set up the environment.
    pause
    exit /b 1
)
REM Check if Python is installed
venv\Scripts\python.exe --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH >> service.log
    echo Please install Python 3.7 or higher
    pause
    exit /b 1
)

REM Start the application using virtual environment venv\Scripts\python.exe
REm venv\\Scripts\\activate.bat
rem waitress-serve --port=8080 app:app


start /b "" venv\Scripts\pythonw.exe -m waitress --port=8080 app:app

exit