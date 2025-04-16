#input 输入时，将输入对象视为字符串，当输入数字时不可以进行运算
age = input("what is you age? ")
print(age)

# ages = age + 1            #报错，因为age出来作为字符串，不可以运算
# print(ages)          

# 输入为数字时，要转化为可以运算的 ，但是int只能搞定整数的，
age = float(age)
ages = age + 1
print({ages, 7})             # 四舍五入去7位小数