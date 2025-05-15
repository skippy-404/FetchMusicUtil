import requests


def download_mp4(url,song_name):
    response = requests.get(url)
    response.raise_for_status()
    import os
    mp4_folder = os.path.join(os.path.dirname(__file__), '../mp4')
    os.makedirs(mp4_folder, exist_ok=True)
    file_path = os.path.join(mp4_folder, song_name + '.mp4')
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print('文件下载成功')