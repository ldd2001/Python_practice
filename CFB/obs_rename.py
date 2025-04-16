import os

# 在代码的开头设置文件夹路径，方便修改
base_dir = r"C:/Users/ldd20/Desktop/INLET_V35"  # 请修改为你的目标文件夹路径

def rename_folders_and_files(base_dir):
    # 第一步：遍历文件夹，删除所有后缀为 ".old" 的文件
    for root, dirs, files in os.walk(base_dir, topdown=False):
        for file in files:
            if file.endswith('.old'):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"删除文件: {file_path}")

    # 第二步：遍历文件夹，重命名所有文件夹
    for root, dirs, files in os.walk(base_dir):
        for dir_name in dirs:
            if 'v40' in dir_name:
                old_dir_path = os.path.join(root, dir_name)
                new_dir_name = dir_name.replace('v40', 'v35')
                new_dir_path = os.path.join(root, new_dir_name)
                os.rename(old_dir_path, new_dir_path)
                print(f"重命名文件夹: {old_dir_path} -> {new_dir_path}")

    # 第三步：遍历文件，重命名所有的文件
    for root, dirs, files in os.walk(base_dir):
        for file_name in files:
            if 'v40' in file_name:
                old_file_path = os.path.join(root, file_name)
                new_file_name = file_name.replace('v40', 'v35')
                new_file_path = os.path.join(root, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(f"重命名文件: {old_file_path} -> {new_file_path}")

if __name__ == '__main__':
    if os.path.isdir(base_dir):
        rename_folders_and_files(base_dir)
    else:
        print("指定的路径不是一个有效的文件夹。")
