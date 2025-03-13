players = ['charles','martina','michael','florence','eli']

# 打印一部分列表

#1. [a,b]代表从索引a开始，输出个数为b-a个元素
print(players[0:3])     #输出players从0开始，0,1,2三个元素
print(f"three palyers is {players[0:3]}")

#提取第234个元素
print(players[1:4])

#[:b] 索引将从0开始
print(players[:4])

#[a:] 索引从a开始，直到列表结束
print(players[2:])

#[-a:] 打印最后a个元素组成的列表
print(players[-3:])

#[a:b:c] 从索引a开始，到b结束，间隔一个打印出来
print(players[0:5:2])    
#表格里有5个元素，索引分别为0,1,2,3,4。a要从0开始，b就是元素个数，要比索引多1，间隔：打印第一个第三个，间隔为3-1=2

#2. 遍历列表部分元素 for循环 这个打印出来不是列表了
for player in players[:3]:
    print(player)

for player1 in players[-3:][::-1]:  #[::-1]代表对切片结果进行翻转，最后一个变成第一个，以此类推
    print(player1)


#3. 复制列表[:]
my_foods = ['pizza','ice-cream','hamburger']
friend_foods = my_foods[:]
print(f"My food is {my_foods}")
print(f"Friends food is {friend_foods}")
#这是两个元素上相同的列表，是两个列表
my_foods.append('bbq')
my_foods.insert(1,'huoguo')
friend_foods.append('huoguo')
friend_foods.insert(0,'bbq')
print(f"My new food is {my_foods}")
print(f"Friends new food is {friend_foods}")