import requests
import os

url = input("vvedite :")

r = requests.get(url, stream=True)

if r.status_code == 200:
    file_extension = ".mp4"
    file_name = 'videooo' + file_extension

    with open(file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    print(f"Video saved as {file_name}")
else:
    print("Error downloading video")
