# 确定平均时间开始使用，将tecplot导出的二维文件导入，每隔100计算步输出数据
# barracuda重新计算时不会删除未保存的数据，可能会出现折线图的短线，检查删除即可

import os
import pandas as pd

# 设置文件夹路径
folder_path = 'C:/Users/ldd20/Desktop/SHIJUN'
file_names = ['t', 'y6', 'y9', 'y12']  # 文件名列表

# 初始化一个空的DataFrame用于合并数据
combined_data = pd.DataFrame()

for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    
    if not os.path.exists(file_path):
        print(f"文件 '{file_name}' 未找到")
        continue  # 跳过不存在的文件

    try:
        # 读取数据并转换为数值类型
        data = pd.read_csv(file_path, sep=r'\s+', header=None)
        data = data.apply(pd.to_numeric, errors='coerce')
        
        # 提取每隔100行数据并重置索引（确保行号对齐）
        sampled_data = data.iloc[::100].reset_index(drop=True)
        
        # 将数据添加到合并DataFrame（每个文件作为一列）
        # 假设所有文件数据列数一致，取第一列数据
        combined_data[file_name] = sampled_data.iloc[:, 0]  # 只取第一列
        
        print(f"文件 '{file_name}' 已处理")
        
    except Exception as e:
        print(f"处理文件 '{file_name}' 时出错: {e}")

# 导出合并后的数据到Excel
output_path = os.path.join(folder_path, "combined_results.xlsx")
combined_data.to_excel(output_path, index=False, engine='openpyxl')
print(f"\n所有文件已合并至: {output_path}")