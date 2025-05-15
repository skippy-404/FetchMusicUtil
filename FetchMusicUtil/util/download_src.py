
import os
import requests
import hashlib
import platform


def download_file(share_url, song_name=None):
    try:

        mp4_folder = os.path.join(os.path.dirname(__file__), '../src')
        os.makedirs(mp4_folder, exist_ok=True)
        if song_name:
            file_name = song_name 
        else:
            file_name = hashlib.md5(share_url.encode('utf-8')).hexdigest() + '.mp4'
        file_path = os.path.join(mp4_folder, file_name)
        download_response = requests.get(share_url)
        download_response.raise_for_status()
        with open(file_path, 'wb') as file:
            file.write(download_response.content)
        print(f'文件 {file_name} 下载成功，保存路径: {file_path}')
    except requests.exceptions.HTTPError as http_err:
        print(f'下载文件时发生 HTTP 错误: {http_err}')
    
