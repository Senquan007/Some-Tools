
'''
使用说明：
在输入目录，该脚本只会对该目录下的文件夹进行搜查，
如输入 /Video/red （该文件下有xml、mp4文件）
但是该脚本无法正常运行
输入 /Video
该脚本才会正确的对red文件夹内的视频进行转换
'''

import os
import danmaku2ass
import difflib


def find_matching_mp4(xml_file, folder_path):
    """
    根据 XML 文件的文件名，在指定文件夹内查找最相似的 MP4 文件。
    通过文件名的前缀或相似度进行匹配。
    """
    xml_filename = os.path.splitext(xml_file)[0]  # 获取去掉扩展名的文件名
    mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]

    # 使用 difflib 对文件名进行模糊匹配，返回最相似的文件
    best_match = None
    highest_ratio = 0
    for mp4_file in mp4_files:
        mp4_filename = os.path.splitext(mp4_file)[0]
        # 计算文件名的相似度
        ratio = difflib.SequenceMatcher(None, xml_filename, mp4_filename).ratio()
        if ratio > highest_ratio:
            best_match = mp4_file
            highest_ratio = ratio

    return best_match


def convert_xml_to_ass_in_folder(folder_path):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.xml'):
                # 获取 XML 文件路径
                input_file = os.path.join(root, file)

                # 查找与 XML 文件匹配的 MP4 文件
                matching_mp4 = find_matching_mp4(file, root)

                if matching_mp4:
                    # 获取 MP4 文件路径
                    mp4_file = os.path.join(root, matching_mp4)

                    # 获取 ASS 文件的输出路径，与 MP4 文件同名
                    output_file = os.path.join(root, file.replace('.xml', '.ass'))

                    # 调用 Danmaku2ASS 函数进行转换
                    try:
                        danmaku2ass.Danmaku2ASS(
                            input_files=input_file,  # 输入文件路径
                            input_format='autodetect',  # 自动检测输入格式
                            output_file=output_file,  # 输出文件路径
                            stage_width=1920,  # 舞台宽度
                            stage_height=1080,  # 舞台高度
                            font_size=35.0,  # 字体大小
                            text_opacity=0.8,  # 文本不透明度
                            duration_marquee=10.0,  # 滚动弹幕显示的持续时间
                            duration_still=5.0,  # 静止弹幕显示的持续时间
                            reserve_blank=0,  # 保留底部空白高度
                            font_face='黑体'  # 字体名称
                        )
                        print(f"Successfully converted {input_file} to {output_file}")

                        # 删除原有的 XML 文件
                        os.remove(input_file)
                        print(f"Deleted {input_file}")
                    except Exception as e:
                        print(f"Error converting {input_file}: {e}")
                else:
                    print(f"No matching MP4 file found for {input_file}, skipping conversion.")


# 获取用户输入的根目录
base_dir = input("请输入文件夹路径：")

# 遍历用户输入的目录下的所有文件夹
for root, dirs, files in os.walk(base_dir):
    for dir in dirs:
        folder_path = os.path.join(root, dir)
        print(f"Processing folder: {folder_path}")
        convert_xml_to_ass_in_folder(folder_path)
