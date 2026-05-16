@echo off
cd /d "%~dp0"
REM Uses Python 3.10 launcher if available; falls back to default python.
where py >nul 2>&1
if %ERRORLEVEL%==0 (
  py -3.10 daily_52_week_report.py
) else (
  python daily_52_week_report.py
)
