"""
YouTube 影片下載腳本 - 下載為 MP4 格式
使用 yt-dlp 套件
"""
import yt_dlp
import os

# 下載的影片 URL（單一影片或播放清單）
URL = "https://www.youtube.com/watch?v=2hbYCe_E5aU&list=PLWWZkn1dW3eAvSZfJv0-02q27JIsfbN2f"

# 輸出資料夾（可自行修改）
OUTPUT_DIR = "downloads"

def download_video(url: str, output_dir: str = OUTPUT_DIR):
    """下載 YouTube 影片為 MP4"""
    os.makedirs(output_dir, exist_ok=True)
    
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        "postprocessors": [{
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4",
        }],
        "noplaylist": True,  # 只下載單一影片，不整份播放清單
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("下載完成！檔案位於:", os.path.abspath(output_dir))

if __name__ == "__main__":
    download_video(URL)
