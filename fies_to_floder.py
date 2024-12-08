# 该脚本用于识别某一目录同名文件，并将该文件转入同一文件夹内


import os
import shutil


def move_files_to_named_folders(src_dir):
    # 创建一个字典来存储前缀和对应的文件列表
    prefix_dict = {}

    # 遍历源目录中的所有项
    for item in os.listdir(src_dir):
        # 构建完整路径
        item_path = os.path.join(src_dir, item)

        # 只处理文件，忽略目录
        if os.path.isfile(item_path):
            # 提取文件名中的共同前缀（这里假设前缀是文件名的一部分）
            # 你可以根据实际情况调整这个逻辑，比如使用正则表达式或字符串分割
            prefix = item.split(' [')[0]  # 假设前缀是文件名中' ['之前的部分

            # 将文件添加到对应前缀的列表中
            if prefix in prefix_dict:
                prefix_dict[prefix].append(item)
            else:
                prefix_dict[prefix] = [item]

    # 遍历前缀字典，为每个有超过两个文件的前缀创建一个文件夹，并移动文件
    for prefix, files in prefix_dict.items():
        # 只有当文件数量大于2时才执行操作
        if len(files) > 2:
            # 构建目标文件夹路径
            dest_folder = os.path.join(src_dir, prefix)

            # 如果文件夹不存在，则创建它
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            # 移动文件到目标文件夹
            for file in files:
                shutil.move(os.path.join(src_dir, file), os.path.join(dest_folder, file))


# 指定源目录路径（使用原始字符串来避免转义字符问题）
source_directory = input("Please input the path:")
# 调用函数执行操作
move_files_to_named_folders(source_directory)

print("Files have been moved to their respective named folders based on prefix (if more than two files per prefix).")