# Registers a Windows Task Scheduler job to run the report daily at 7:00 AM (local PC only).
# For cloud scheduling (PC off), use GitHub Actions: .github/workflows/stock_52_week_report.yml
# Run once in PowerShell:  .\register_morning_task.ps1

$TaskName = "Stock52WeekDailyReport"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$BatchPath = Join-Path $ScriptDir "run_daily_report.bat"

$Action = New-ScheduledTaskAction -Execute $BatchPath -WorkingDirectory $ScriptDir
$Trigger = New-ScheduledTaskTrigger -Daily -At 7:00AM
$Settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopOnIdleEnd

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $Action `
    -Trigger $Trigger `
    -Settings $Settings `
    -Description "Email S&P/Dow/NASDAQ stocks at 52-week highs and lows" `
    -Force

Write-Host "Scheduled task '$TaskName' registered (daily at 7:00 AM)."
Write-Host "Test now: $BatchPath"
