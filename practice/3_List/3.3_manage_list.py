# 定义列表
cars = ['bmw','subaru','toyota','nissan','audi']

#1. sort() 永久排序：依照首位字母顺序排列各元素。注意：当元素中存在大写的首位字母，优先排列大写
cars.sort()
print(f"{cars}\n")

cars.sort(reverse=True)   #reverse=True 倒序排列
print(f"{cars}\n")
#该方法排序是永久排序，列表内部顺序永久变化


#2. sorted() 临时排序：按照特定的顺序显示列表
cars1 = ['bmw','subaru','toyota','nissan','audi']
print(f"Here is the original list:\n{cars1}\n")            #打印原始列表
print(f"Here is the sorted list:\n{sorted(cars1)}\n")      #打印临时排序列表
print(f"Here is the reverse sorted list:\n{sorted(cars1,reverse=True)}\n")                     #打印临时倒序列表
print(f"{cars1}\n")

#3. reverse() 反向打印列表，并不是按照字母顺序，按照已经给出的顺序,会改变列表顺序
cars2 = ['bmw','subaru','toyota','nissan','audi']
cars2.reverse()
print(f"{cars2}\n")

#4. len() 确定列表长度  即元素个数
cars3 = ['bmw','subaru','toyota','nissan','audi']
print(f"List cars3 is {len(cars3)}\n")