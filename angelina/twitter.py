"""kutman"""
# TODO: add more functionality
import requests

url = input("Введите ссылку видео из X (Twitter) :")

r = requests.get(url, stream=True)

if r.status_code == 200:
    with open('videofromtwitter.mp4', 'wb') as f:
        for chunk in r:
            f.write(chunk)
    print(" Видео сохранил в текущей директории")
else:
    print("Error downloading video")

# TODO : 1.Скачать видео >>>
# TODO : 2.Передать ссылку через переменную >>
# TODO : 3.Добавить цикл WHILE чтобы оно спрашивала бесконечно
# TODO : 4.Добавить опратор break "стоп/stop" когда вместо ссылки передает

