
from pytube import YouTube

youtube_video_url = 'https://www.youtube.com/watch?v=9MiFRbymQXQ'

try:
    yt_obj = YouTube(youtube_video_url)

    yt_obj.streams.get_audio_only().download(output_path='D:/Web Development/Python/youtube - vdo - donwloader', filename='audio')
    print('YouTube video audio downloaded successfully')
except Exception as e:
    print(e)