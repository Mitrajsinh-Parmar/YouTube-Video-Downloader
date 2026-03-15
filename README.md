# YouTube Video Downloader

A streamlined Python utility designed to download YouTube videos without the need for external dependencies like FFmpeg. This script is specifically configured to handle the "SABR" and JavaScript-based playback errors common in 2026 by leveraging mobile client emulation.

## ✨ Features

* **No FFmpeg Required**: Specifically targets "single-file" formats where audio and video are already merged.
* **Android Client Emulation**: Uses the `android` player client to improve reliability and bypass modern web-client restrictions.
* **MP4 Focused**: Prioritizes the `.mp4` extension for maximum compatibility across devices.
* **Lightweight**: Only requires the `yt-dlp` library.

## ⚙️ Installation

1.  **Clone or download** the `app.py` file.
2.  **Install the dependency**:
    ```bash
    pip install yt-dlp
    ```
