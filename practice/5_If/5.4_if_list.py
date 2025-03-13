#列表if
ages = ['1','2','3']
for age in ages:
    print(f"age is {age}\n")

##条件列表
requested_foods = ['mushrooms','green peppers','extra cheese']
for requested_food in requested_foods:
    if requested_food == 'green peppers':
        print(f"Sorry, we don't have {requested_food}")
    else:
        print(f"Adding {requested_food}")
print("\n")
# 改进结果并不好，sorry打印出来在中间，不好看，如果把不存在的食物放在最后打印出来
#代码修改如下，此时可以创建一个空列表
requested_foods_1 = ['mushrooms','green peppers','extra cheese']
unaviliab_foods = []                                               #创建空列表，将没有的食物放进去，临时存储一下然后最后打印出来
for requested_food_1 in requested_foods_1:
    if requested_food_1 == 'green peppers':        # 如果 green在，那么把他加入到空列表中，第一次循环，mushroom，if is false，执行else，输出mush
        unaviliab_foods.append(requested_food_1)   # 第二次循环， green在，if is true 那么执行if，将他加入空列表中
    else:
        print(f"Adding {requested_food_1}")
print(f"Sorry, we don't have {' '.join(unaviliab_foods)}")    # 可以输出列表中的元素内容

#多列表交叉使用



