@echo off
cd /d "%~dp0"
echo Installing dependencies for Python 3.10...
py -3.10 -m pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
  echo Install failed. Ensure Python 3.10 is installed: py -3.10 --version
  exit /b 1
)
echo.
echo Done. Next: copy config.example.env to config.env and add your email settings.
echo Test: py -3.10 daily_52_week_report.py --dry-run --limit 50
