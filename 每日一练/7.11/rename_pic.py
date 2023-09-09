import os

# 定义目录路径和重命名的起始序号
directory = r"C:\Users\DELL123\Desktop\study\爬虫项目\每日一练\7.11\爬取的知乎图片"
start_index = 1
print(os.listdir(directory))

# 遍历目录下的文件
for filename in os.listdir(directory):
    # 检查文件是否是jpg或png文件
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 获取文件的完整路径
        filepath = os.path.join(directory, filename)

        # 构造新的文件名
        new_filename = str(start_index) + filename[-4:]

        # 构造新的文件路径
        new_filepath = os.path.join(directory, new_filename)

        # 在重命名之前，检查新的文件名是否已存在
        if os.path.exists(new_filepath):
            print(f"File {new_filepath} already exists, skip renaming.")
            start_index +=1
            continue

        # 重命名文件
        os.rename(filepath, new_filepath)

        # 增加序号
        start_index += 1
