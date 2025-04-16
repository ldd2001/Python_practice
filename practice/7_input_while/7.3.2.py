# 删除包含特定值的所有列表元素
pets = ['dogs','cats','birds','cats','pigs']

while 'cats' in pets:
    pets.remove('cats')

for pet in pets:
    print(pet)