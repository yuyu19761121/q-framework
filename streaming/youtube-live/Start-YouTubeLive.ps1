param(
  [string]$ConfigPath = ""
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path

if (!$ConfigPath) {
  $ConfigPath = Join-Path $Root "config.json"
}

$Cfg = Get-Content $ConfigPath -Raw | ConvertFrom-Json
$Ffmpeg = $env:FFMPEG_PATH
$Chrome = $env:CHROME_PATH
$Profile = Join-Path $Root "chrome-profile"
$LogDir = Join-Path $Root "logs"
$KeyFile = Join-Path $Root "youtube-stream-key.txt"
$PidFile = Join-Path $Root "streamer-pids.json"

if ([string]::IsNullOrWhiteSpace($Ffmpeg) -or !(Test-Path $Ffmpeg)) {
  throw "Set FFMPEG_PATH to ffmpeg.exe."
}
if ([string]::IsNullOrWhiteSpace($Chrome) -or !(Test-Path $Chrome)) {
  throw "Set CHROME_PATH to chrome.exe."
}

New-Item -ItemType Directory -Force -Path $LogDir,$Profile | Out-Null

$key = $env:YOUTUBE_STREAM_KEY
if ([string]::IsNullOrWhiteSpace($key) -and (Test-Path $KeyFile)) {
  $key = (Get-Content $KeyFile -Raw).Trim()
}
if ([string]::IsNullOrWhiteSpace($key)) {
  throw "YouTube stream key missing."
}

$target = ([string]$Cfg.rtmps_base).TrimEnd("/") + "/" + $key
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$log = Join-Path $LogDir "youtube-live-$stamp.log"

$chromeArgs = @(
  "--user-data-dir=$Profile",
  "--app=$($Cfg.source_url)",
  "--window-position=0,0",
  "--window-size=$($Cfg.capture_width),$($Cfg.capture_height)",
  "--force-device-scale-factor=0.8",
  "--disable-session-crashed-bubble",
  "--disable-infobars",
  "--no-first-run"
)

$chromeProc = Start-Process -FilePath $Chrome -ArgumentList $chromeArgs -PassThru
Start-Sleep -Seconds 5

@{
  chrome_pid = $chromeProc.Id
  supervisor_pid = $PID
  started_at = (Get-Date).ToString("o")
} | ConvertTo-Json | Set-Content -Encoding UTF8 $PidFile

while ($true) {
  $vf = "scale=$($Cfg.output_width):$($Cfg.output_height):force_original_aspect_ratio=decrease,pad=$($Cfg.output_width):$($Cfg.output_height):(ow-iw)/2:(oh-ih)/2:black,format=yuv420p"

  $Args = @(
    "-hide_banner","-loglevel","info",
    "-f","gdigrab","-framerate","$($Cfg.fps)",
    "-video_size","$($Cfg.capture_width)x$($Cfg.capture_height)","-i","desktop",
    "-f","lavfi","-i","anullsrc=channel_layout=stereo:sample_rate=48000",
    "-vf",$vf,
    "-c:v","h264_nvenc","-preset","p4","-tune","ll","-rc","cbr",
    "-b:v","$($Cfg.video_bitrate)",
    "-maxrate","$($Cfg.video_maxrate)",
    "-bufsize","$($Cfg.video_bufsize)",
    "-g","$([int]$Cfg.fps * 2)","-bf","2",
    "-c:a","aac","-b:a","$($Cfg.audio_bitrate)","-ar","48000",
    "-f","flv",$target
  )

  & $Ffmpeg @Args 2>&1 | Tee-Object -FilePath $log -Append
  Start-Sleep -Seconds 10
}
