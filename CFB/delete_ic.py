import os

def delete_ic_files(folder_path):
    # 排除不删除的文件名列表
    excluded_files = ["IC_1.000e+01", "IC_"]
    
    # 遍历目标文件夹及其子文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 如果文件名以"IC"开头且不在排除列表中，删除文件
            if file.startswith("IC") and file not in excluded_files:
                file_path = os.path.join(root, file)
                try:
                    # 删除文件
                    os.remove(file_path)
                    print(f"已删除文件: {file_path}")
                except Exception as e:
                    print(f"无法删除文件 {file_path}: {e}")

if __name__ == "__main__":
    # 设置目标文件夹路径
    folder_path = r"E:/RIGHT MODEL"
    
    # 调用函数删除文件
    delete_ic_files(folder_path)
