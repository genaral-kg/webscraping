# import requests
# import youtube_dl
#
# url = 'https://www.youtube.com/watch?v=8iH2qIWZBwk'
#
# ydl_opts = {}
#
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     info_dict = ydl.extract_info(url, download=False)
#     video_url = info_dict.get("url", None)
#     if video_url:
#         with requests.get(video_url, stream=True) as response:
#             if response.status_code == 200:
#                 file_name = info_dict.get("title", "video") + ".mp4"
#                 with open(file_name, 'wb') as f:
#                     for chunk in response.iter_content(chunk_size=1024):
#                         if chunk:
#                             f.write(chunk)
#                 print(f"Видео успешно скачано как {file_name}")
#             else:
#                 print("Ошибка загрузки видео")
#     else:
#         print("Ошибка получения URL видео")

# TODO : ютуб код работает но только для доступных всем а для возрастных ограничений не работает



#from pytube import YouTube
#url = input("Ссылка с ютуба : ")

# Создайте объект YouTube
#yt = YouTube(url)

# Выберите поток с наилучшим качеством видео и аудио
#video_stream = yt.streams.get_highest_resolution()

# Загрузите видео
#video_stream.download()

#print(f"Видео \"{yt.title}\" успешно скачано")

from pytube import YouTube

url = input("Ссылка с ютуба : ")

# Создайте объект YouTube
yt = YouTube(url)

# Получите поток с разрешением 1080p и аудиодорожкой
video_stream = yt.streams.filter(res="1080p", type="video").first()

# Установите качество звука
video_stream.set_audio_quality(audio_quality="high")

# Загрузите видео
video_stream.download()

print(f"Видео \"{yt.title}\" успешно скачано")



"""


# the function takes the video url as an argument
def video_downloader(video_url):
    # passing the url to the YouTube object
    my_video = YouTube(video_url)
    # downloading the video in high resolution
    my_video.streams.get_highest_resolution().download()
    # return the video title
    return my_video.title


# the try statement will run if there are no errors
try:
    # getting the url from the user
    youtube_link = input('Enter the YouTube link:')
    print(f'Downloading your Video, please wait.......')
    # passing the url to the function
    video = video_downloader(youtube_link)
    # printing the video title
    print(f'"{video}" downloaded succussfully!!')
# the except will catch ValueError, URLError, RegexMatchError and simalar
except:
    print(f'Failed to download video\nThe ' \
          'following might be the causes\n->No internet ' \
          'connection\n->Invalid video link')
"""


