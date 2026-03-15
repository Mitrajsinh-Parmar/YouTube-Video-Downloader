import yt_dlp

def download_video_no_ffmpeg(url):
    ydl_opts = {
        # 'best' is the key here to get a single file (no FFmpeg needed)
        # We also specifically exclude formats that require merging
        'format': 'best[ext=mp4]/best',
        
        # This is the 2026 fix: Change the "client" to Android
        # It's less likely to trigger the JavaScript/SABR errors
        'extractor_args': {
            'youtube': {
                'player_client': ['android'],
            }
        },
        
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Attempting to download using Android client: {url}")
            ydl.download([url])
            print("\nDownload finished!")
    except Exception as e:
        print(f"Error: {e}")
        print("\nNote: If this still fails, YouTube may have fully blocked ")
        print("no-FFmpeg downloads for this specific video.")

if __name__ == "__main__":
    link = input("Enter YouTube URL: ").strip()
    download_video_no_ffmpeg(link)