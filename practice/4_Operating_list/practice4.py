#4.3 
values = list(range(1,21))
for value in values:
    print(value)

#4.4
values_singal = list(range(1,20,2))
for value_singal in values_singal:
    print(value_singal)

#4.9 生成列表
cube = [value1**3 for value1 in range(1,11)]
print(cube)

cube_1 = [value2**3 for value2 in range(1,11,2)]
print(cube_1)