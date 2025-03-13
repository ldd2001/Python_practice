cars= ['audi','bmw','bugati','toyota']
for car in cars:
    if car == 'bmw':                   #检查名字是否是bmw，是的话就大写，不是就小写
        print(car.upper())             # = 代表赋值，将后面的值赋给前面的变量
    else:                              # == 相等运算符，检查变量的值是否是后面的
        print(car.lower())
print("\n")


# != 不等运算符
request_food = ['mushroom']
for food in request_food:
    if food == 'mush':          #检查food是不是mushroom，是的话输出ok，不是就输出nook
        print("ok")
    else:
        print("no ok")


# 检查多个条件
