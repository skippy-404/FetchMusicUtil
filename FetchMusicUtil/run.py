from util.API import fetch_music
from util.download_src import download_file
from util.download_mp4 import download_mp4
from util.search_url import find_song_url

share_url,track_id, song_name = fetch_music('床')

print(f'share_url{share_url}获取到的track_id: {track_id}，歌曲名: {song_name}')
download_file(share_url, song_name)
URL_list = find_song_url(song_name)
if URL_list:
    import json
    URL = json.loads(URL_list[0]) if URL_list else None
    if URL:
        download_mp4(URL, song_name)
else:
    print(f'未找到 {song_name} 的有效下载链接，跳过下载。')
    