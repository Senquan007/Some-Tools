import os
import subprocess


def extract_audio_from_videos(input_folder, output_folder):
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹下的所有文件
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # 检查文件是否为视频文件（可以根据需要扩展此列表）
        if filename.endswith(('.mp4', '.mkv', '.avi', '.mov')):
            # 设置输出文件名和路径
            output_filename = os.path.splitext(filename)[0] + ".flac"
            output_path = os.path.join(output_folder, output_filename)

            # 使用FFmpeg提取音频并保存为FLAC格式
            command = [
                'ffmpeg',
                '-i', input_path,  # 输入视频文件
                '-vn',  # 忽略视频流
                '-acodec', 'flac',  # 使用FLAC格式
                output_path  # 输出文件路径
            ]

            # 执行FFmpeg命令
            subprocess.run(command, check=True)
            print(f"已成功提取音频：{output_filename}")


# 定义输入文件夹和输出文件夹路径
input_folder = '..\视频'
output_folder = '..\音频'

# 执行音频提取
extract_audio_from_videos(input_folder, output_folder)
