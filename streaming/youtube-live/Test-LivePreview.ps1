param(
  [string]$SourceUrl = "https://studio.havefun.buzz/customer-live/",
  [int]$Seconds = 12
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Ffmpeg = $env:FFMPEG_PATH
$Chrome = $env:CHROME_PATH
$Profile = Join-Path $Root "chrome-profile"
$Out = Join-Path $Root "preview.mp4"

if ([string]::IsNullOrWhiteSpace($Ffmpeg) -or !(Test-Path $Ffmpeg)) {
  throw "Set FFMPEG_PATH to ffmpeg.exe."
}
if ([string]::IsNullOrWhiteSpace($Chrome) -or !(Test-Path $Chrome)) {
  throw "Set CHROME_PATH to chrome.exe."
}

if (Test-Path $Out) { Remove-Item $Out -Force }

$chromeArgs = @(
  "--user-data-dir=$Profile",
  "--app=$SourceUrl",
  "--window-position=0,0",
  "--window-size=1024,768",
  "--force-device-scale-factor=0.8",
  "--disable-session-crashed-bubble",
  "--disable-infobars",
  "--no-first-run"
)

$ChromeProc = Start-Process -FilePath $Chrome -ArgumentList $chromeArgs -PassThru
Start-Sleep -Seconds 5

try {
  $Args = @(
    "-hide_banner","-loglevel","warning","-y",
    "-f","gdigrab","-framerate","30","-video_size","1024x768","-i","desktop",
    "-f","lavfi","-i","anullsrc=channel_layout=stereo:sample_rate=48000",
    "-t","$Seconds",
    "-vf","scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:black,format=yuv420p",
    "-c:v","h264_nvenc","-preset","p4","-tune","ll","-rc","cbr",
    "-b:v","4500k","-maxrate","4500k","-bufsize","9000k","-g","60","-bf","2",
    "-c:a","aac","-b:a","128k","-ar","48000",
    "-movflags","+faststart",$Out
  )

  & $Ffmpeg @Args

  if (!(Test-Path $Out)) {
    throw "Preview file was not created."
  }
}
finally {
  Get-CimInstance Win32_Process |
    Where-Object { $_.Name -eq "chrome.exe" -and $_.CommandLine -like "*$Profile*" } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
}
