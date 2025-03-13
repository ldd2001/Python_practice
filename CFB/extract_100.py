import os
import pandas as pd

# 设置文件夹路径
folder_path = 'C:/Users/ldd20/Desktop/Time_averged'  # 替换为你的文件夹路径

# 获取文件名列表
file_names = ['t', 'y5', 'y6', 'y9', 'y12','OUTLET']  # 文件名列表

# 循环处理每个文件
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)  # 拼接文件路径
    
    if os.path.exists(file_path):
        # 读取文件内容，假设数据是以空格或制表符分隔的
        try:
            # 使用原始字符串表示正则表达式
            data = pd.read_csv(file_path, sep=r'\s+', header=None)  # 使用正则匹配空格或制表符作为分隔符
            
            # 检查数据类型并转换为数字
            data = data.apply(pd.to_numeric, errors='coerce')  # 转换文本为数字，无法转换的值会变为 NaN
            
            # 提取每隔100行的数据
            sampled_data = data.iloc[::100]  # 每隔100行提取一次数据
            
            # 导出到 Excel
            excel_file_path = os.path.join(folder_path, f"{file_name}_extracted.xlsx")
            sampled_data.to_excel(excel_file_path, index=False, engine='openpyxl')
            print(f"File '{file_name}' has been processed and exported to Excel.")
        
        except Exception as e:
            print(f"Error processing file '{file_name}': {e}")
    else:
        print(f"File '{file_name}' not found.")
