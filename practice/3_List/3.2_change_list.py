origin_motorcycles = ['hOnda','Yamaha','SuzukI']

motor1 = f"{origin_motorcycles[0].lower()}"
motor2 = f"{origin_motorcycles[1].lower()}"
motor3 = f"{origin_motorcycles[2].lower()}"
print(f"{motor1}\n")

motorcycles = [motor1,motor2,motor3]            #变量是可以加入数组中的
print(f"{motorcycles}\n")

#修改列表中的元素，将列表中第0个元素更改为ducati，并输出
#修改后，列表变化，不是以前的列表，以后的操作都在修改后的列表上进行
motorcycles[0] = 'ducati'
print(f"{motorcycles}\n")

#1.添加元素.append()：将新元素追加到列表末尾。可以创建一个空列表，然后利用.append()添加新元素
motorcycles.append('ducati')
print(f"{motorcycles}\n")

#2.插入元素.insert(),将toyota放入列表第一个位置，其余元素依次向后排列
motorcycles.insert(0,'toyota')     #第一个位置，索引为0
print(f"{motorcycles}\n")

motorcycles.insert(2,"nsx")        #在列表的第三个位置加入，索引为2
print(f"{motorcycles}\n")


#3.1删除元素：del 已知索引，删除该索引上的元素，可以删除任意位置，del后该元素不再使用
del motorcycles[-1]                #删除该列表最后一个元素，
print(f"{motorcycles}\n")

#3.2提取元素.pop()
# 删除列表 末尾的元素,()就是删除最后，(0)就是删除索引为0的元素
# 用意：相当于把列表中的某个元素提取出来，将其赋值给了·一个新的变量
popped_motocycles = motorcycles.pop()
print(f"{motorcycles}\n")
print(f"{popped_motocycles}\n")

#4根据值删除元素.remove()
motorcycles.remove('nsx')  #指定值为nsx的元素，将其删除
print(f"{motorcycles}\n")
#4.1 remove只能删除一个值为指定值的元素，当列表中有多个相同的值的时候，只会删除第一个
motorcycles.append('nsx')
motorcycles.insert(1,'nsx')      #更改列表内容，加入相同的元素‘nsx’
print(f"{motorcycles}\n")
motorcycles.remove('nsx')        #删除nsx，但列表中存在多个nsx，只会删除第一个 
print(f"{motorcycles}\n")

#除了直接在remove()中写入删除的元素外，也可以使用变量
too_expensive = 'nsx'
motorcycles.remove(too_expensive)
print(f"{motorcycles}\n")