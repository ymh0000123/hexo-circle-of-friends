import os

# 设置目录路径
directory = '.'

# 遍历目录中的文件
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)  # 获取文件的完整路径
    # 检查是否是文件，并且不是data.json也不是sc.py
    if os.path.isfile(file_path) and filename not in ['data.json', 'sc.py']:
        os.remove(file_path)  # 删除文件

print("File deleted successfully")  # 打印删除成功消息
