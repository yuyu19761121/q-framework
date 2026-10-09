# Q-Framework YouTube Live relay

This directory contains a **sanitized reference implementation** for relaying the public Q-Framework Live Compute page to YouTube Live.

It intentionally excludes production hostnames, private paths, internal topology, credentials, stream keys and scheduler details.

## Flow

```text
Q-Framework public live page
  -> dedicated Chromium capture session
  -> FFmpeg H.264/AAC encoder
  -> YouTube RTMPS ingest
```

## Recommended encoder profile

- Output: 1280x720
- Frame rate: 30 fps
- Video codec: H.264
- Video bitrate: 4500 kbps CBR
- Keyframe interval: 2 seconds
- Audio: AAC stereo, 128 kbps
- Transport: RTMPS

The page remains read-only. Streaming must not restart, stop, clear or modify production compute workers.

## Secrets

Never commit a YouTube stream key. Supply it only through:

- `YOUTUBE_STREAM_KEY` environment variable, or
- a local `youtube-stream-key.txt` file excluded by `.gitignore`.

## Preview

Run:

```powershell
.\Test-LivePreview.ps1
```

Verify the preview before starting a real broadcast.

## Start

Set the two required executable paths and the stream key, then run:

```powershell
$env:CHROME_PATH = "C:\Path\To\chrome.exe"
$env:FFMPEG_PATH = "C:\Path\To\ffmpeg.exe"
$env:YOUTUBE_STREAM_KEY = "<local-secret>"
.\Start-YouTubeLive.ps1
```

For unattended use, run this script from an **interactive logged-in session** or a scheduler configured with an interactive token. Desktop capture generally does not work from Windows Session 0.

## Stop

```powershell
.\Stop-YouTubeLive.ps1
```
