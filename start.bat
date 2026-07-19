@echo off
setlocal EnableExtensions
cd /d "%~dp0"
set "PIP_DISABLE_PIP_VERSION_CHECK=1"

echo Checking Python...
set "PYTHON_CMD="
where py >nul 2>nul
if not errorlevel 1 (
    set "PYTHON_CMD=py -3"
) else (
    where python >nul 2>nul
    if not errorlevel 1 (
        set "PYTHON_CMD=python"
    )
)

if not defined PYTHON_CMD (
    echo Python was not found.
    where winget >nul 2>nul
    if errorlevel 1 (
        echo Please install Python 3.10 or later, then run start.bat again.
        echo Press any key to exit...
        pause >nul
        exit /b 1
    )

    echo Installing Python with winget...
    winget install -e --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements
    if errorlevel 1 (
        echo Python installation failed.
        echo Please install Python 3.10 or later, then run start.bat again.
        echo Press any key to exit...
        pause >nul
        exit /b 1
    )

    where py >nul 2>nul
    if not errorlevel 1 (
        set "PYTHON_CMD=py -3"
    ) else (
        where python >nul 2>nul
        if not errorlevel 1 (
            set "PYTHON_CMD=python"
        )
    )
)

if not defined PYTHON_CMD (
    echo Python was installed, but it is not available in this terminal yet.
    echo Please close this window and run start.bat again.
    echo Press any key to exit...
    pause >nul
    exit /b 1
)

if not exist .venv (
    echo Creating virtual environment...
    %PYTHON_CMD% -m venv .venv
    if errorlevel 1 (
        echo Failed to create the virtual environment.
        echo Press any key to exit...
        pause >nul
        exit /b 1
    )
)

call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo Failed to activate the virtual environment.
    echo Press any key to exit...
    pause >nul
    exit /b 1
)

python --version >nul 2>nul
if errorlevel 1 (
    echo Python was not found in the virtual environment.
    echo Press any key to exit...
    pause >nul
    exit /b 1
)

echo Checking Python requirements...
python -m pip --version >nul 2>nul
if errorlevel 1 (
    echo pip was not found. Installing pip...
    python -m ensurepip --upgrade
    if errorlevel 1 (
        echo Failed to install pip.
        echo Press any key to exit...
        pause >nul
        exit /b 1
    )
)

if exist requirements.txt (
    echo Installing Python requirements...
    python -m pip install --disable-pip-version-check -r requirements.txt
    if errorlevel 1 (
        echo Failed to install Python requirements.
        echo Press any key to exit...
        pause >nul
        exit /b 1
    )
)

echo Checking ffmpeg...
python -c "from src.converter import _resolve_tool_path; print(_resolve_tool_path('ffmpeg'))"
if errorlevel 1 (
    echo ffmpeg was not found and could not be installed automatically.
    echo Please check your internet connection, then run start.bat again.
    echo Press any key to exit...
    pause >nul
    exit /b 1
)

python -m src.run
if errorlevel 1 (
    echo Failed to start the application.
    echo Press any key to exit...
    pause >nul
    exit /b 1
)
