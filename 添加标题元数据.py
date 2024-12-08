import os
import sys
sys.path.append(" D:\Python\Python3117\Lib\site-packages")  # 替换为 mutagen 库的实际路径
from mutagen.flac import FLAC


def set_flac_metadata(folder_path):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # 检查文件是否为 FLAC 文件
            if file_name.lower().endswith('.flac'):
                # 获取文件名（去掉扩展名）作为标题
                title = os.path.splitext(file_name)[0]

                # 加载 FLAC 文件并设置标题
                audio = FLAC(file_path)
                audio['title'] = title

                # 保存更改
                audio.save()
                print(f"已为文件 '{file_name}' 设置标题: {title}")


# 使用示例
folder_path = "F:\IMAGES_Classified\Images\IMG_2024_10_G.E.M\音频"
set_flac_metadata(folder_path)
