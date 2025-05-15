import os
import re

search_url = 'luna.douyinvod.com'
root_dir = '/Users/skippy/Desktop/douyinMusicAPI/src'

def find_song_url(song_name):
    matches = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file == song_name:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if search_url in content:
                            print(f'在文件 {file_path} 中找到目标URL。')
                            new_matches = re.findall(fr'\"[^\"]*{search_url}[^\"]*\"', content)
                            matches.extend(new_matches)
                            for match in new_matches:
                                print(f'提取到的内容: {match}')
                except Exception as e:
                    print(f'读取文件 {file_path} 时出错: {e}')
    return matches