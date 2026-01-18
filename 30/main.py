# python project : Build a youtube Thumbnail Downloader

import re

def get_thumbnail(video_url):
    Pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(Pattern,video_url)

    if match:
        video_id = match.group(1)
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        return thumbnail_url
    else:
        return "Invalid Video Url"
    
url = input("Enter the video url : ")
print(f"Your Thumbnail Link : {get_thumbnail(url)}")