bicycles = ['trek','cannondale','redline','specialized']

print(bicycles)
#打印数组内容
print('bicycles')
#打印bicycles单词，此时bicycles看作字符串，非变量
print(bicycles[0])
#索引从0开始，打印数组bicycles里的第0个元素
print(bicycles[-1]) 
#-1代表数组中最后一个元素,不知数组长度可用
print(bicycles[0].title())
#数组元素看作字符串，因此可以对此进行字符串的所有操作，例如大写第一个字母
print(f"I have a {bicycles[0].upper()}")
#f可以在打印时打印出变量的值
print("I have a {bicycles[0].upper()}")

message = f"I have a {bicycles[0].upper()}"
print(message)
