# 1. range() 生成一系列的数
for value in range(1,5):   #输出1234，没有5.
    print(value)

# 2. list() 创建数值列表:加入range()，会使的range出来的东西全部转化成列表  
numbers0 = list(range(1,6))
print(f"The list is\n{numbers0}") 
#使用range()时，可以指定步长，range(起始数,终止数,间隔)
numbers1 = list(range(2,11,2))
print(f"The numbers1 list is\n{numbers1}") 

# 3. 创建空列表，加入1-10的平方
squares = []
for value in range(1,11):
    squares.append(value**2)                #没有创建临时变量，直接加入
print(f"The squares list is\n{squares}") 
#三行代码创建列表繁琐，一行也可以
squares_one = [value_one**2 for value_one in range(1,11)]
print(f"The squares list is\n{squares_one}")                   #一样的效果
