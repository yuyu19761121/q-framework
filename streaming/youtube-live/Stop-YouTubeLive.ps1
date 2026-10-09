$ErrorActionPreference = "SilentlyContinue"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$PidFile = Join-Path $Root "streamer-pids.json"

if (Test-Path $PidFile) {
  $p = Get-Content $PidFile -Raw | ConvertFrom-Json

  if ($p.supervisor_pid) {
    Stop-Process -Id ([int]$p.supervisor_pid) -Force
  }
  if ($p.chrome_pid) {
    Stop-Process -Id ([int]$p.chrome_pid) -Force
  }
}

Get-CimInstance Win32_Process |
  Where-Object { $_.Name -eq "chrome.exe" -and $_.CommandLine -like "*chrome-profile*" } |
  ForEach-Object { Stop-Process -Id $_.ProcessId -Force }

Remove-Item $PidFile -Force -ErrorAction SilentlyContinue
Write-Output "LIVE_STREAM_STOPPED"
