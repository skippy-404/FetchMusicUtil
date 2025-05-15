
import requests
import platform
import hashlib
def fetch_music(msg='红豆'):
    
    # 设置url
    url = 'https://api.ilingku.com/int/v1/dg_qishui'
    # 分离请求体
    request_data = {
        'msg': msg,
        'format': 'json',
        # 'track_id': '6733376660713768962'
    }
    # 发送post请求
    try:
        response = requests.post(url, data=request_data)
        response.raise_for_status()
        result = response.json()
        # print(result)
        # 尝试提取第一个 track_id 和歌曲名
        track_id = None
        song_name = None
        if isinstance(result, dict) and 'data' in result:
            data = result['data']
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        track_id = item.get('track_id')
                        song_name = item.get('title')  # 假设歌曲名在 'name' 字段
                        if track_id:
                            break
        # 拼接网址
        if track_id:
            share_url = 'https://music.douyin.com/qishui/share/track?track_id=' + str(track_id)
            print(share_url)
        else:
            print('未找到有效的 track_id')
        return share_url,track_id, song_name

    except Exception as err:
        print(f'下载文件时发生其他错误: {err}')