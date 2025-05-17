@echo off
echo Horror Movie Video Processor
echo ===========================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in your PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo and make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

:: Check command line arguments
if "%1"=="" (
    echo Usage:
    echo   run_processor.bat [command]
    echo.
    echo Available commands:
    echo   all         - Run the complete process
    echo   generate    - Generate input file only
    echo   concatenate - Concatenate videos only
    echo   audio       - Add audio to video only
    echo   cleanup     - Clean up temporary files
    echo.
    echo Example:
    echo   run_processor.bat all
    echo   run_processor.bat generate
    echo.
    set /p command=Enter command (default: all): 
) else (
    set command=%1
)

:: Default to 'all' if no command provided
if "%command%"=="" set command=all

:: Run the selected command
echo.
echo Running command: %command%
echo.

if "%command%"=="all" (
    python processor.py
) else if "%command%"=="generate" (
    python generate_input.py
) else if "%command%"=="concatenate" (
    python concatenate_videos.py
) else if "%command%"=="audio" (
    python add_audio.py
) else if "%command%"=="cleanup" (
    python cleanup.py
) else (
    echo Unknown command: %command%
    echo Run without arguments to see available commands.
    exit /b 1
)

if %errorlevel% equ 0 (
    echo.
    echo Command completed successfully!
) else (
    echo.
    echo Command failed! Check error messages above.
)

pause 