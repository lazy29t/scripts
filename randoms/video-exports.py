import os
from instaloader import Instaloader, Post
from pathlib import Path
from moviepy.editor import VideoFileClip

# Path to Downloads folder
downloads_folder = Path.home() / "Downloads"

def download_instagram_video(post_url, download_folder):
    # Initialize Instaloader
    loader = Instaloader()

    # Get post from URL
    post = Post.from_shortcode(loader.context, post_url.split("/")[-2])

    # Download video
    loader.download_post(post, target=str(download_folder))

    # Find the video file
    for file in os.listdir(download_folder):
        if file.endswith(".mp4"):
            video_path = download_folder / file
            return video_path

    raise FileNotFoundError("Video not found in downloaded files.")

# Example Instagram URL
post_url = "https://www.instagram.com/p/VIDEO_SHORTCODE/"

# Run download
try:
    video_path = download_instagram_video(post_url, downloads_folder)
    print(f"Video saved to {video_path}")
except Exception as e:
    print(f"Error: {e}")