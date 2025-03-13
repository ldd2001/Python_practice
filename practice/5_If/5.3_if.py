#1. 简单的if语句   只考虑一个结果
age = 19
if age > 18:
    print("ok")

# 2.if-else       选择只有两个，要么a要么b
age_0 = 17
if age_0 < 18:
    print("no ok\n")
else:
    print("ok\n")

#3. if elif else #选择多个  检查是否符合第一个要求，继续检查是否符合第二个，如果都不是，那就直接执行第三条
age_1 = 45
if age_1 <=8:                             #筛选条件只有一个，也就是age的要求
    print("child,no ticket")
elif age_1 <= 18:
    print("teenage,half ticket")
else:
    print("adult,full ticket")
#简洁代码
age_2 = -1                      #if elif else 会按照顺序执行语句，当某一个条件为True时，执行结束
if age_2 <= 8:
    price = 0
elif age_2 < 18:
    price = 10
else:
    price = 20

print(f"The ticket price is {price}\n")

#practice 5.5
age_3 = 45
if age_3 < 2:
    message = "baby"
elif 2 <= age_3 < 13:
    message = "child"
elif 13 <= age_3 < 18:
    message = "teen"
elif 18 <= age_3 < 65:
    message = "adult"
else:
    message = "old"
print(f"Age is {age_3}, this person is a/an {message}")