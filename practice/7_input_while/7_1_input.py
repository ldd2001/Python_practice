#input()让用户输入一些文本，变量=input（）然后把值赋值给变量
#message = input("Tell me something, and I will repeat it back to you:")
#print(message)

prompt = "If you share....."
prompt += "\nWhat is your name?"   # 等价于 prompt = prompt + "..." 他是一个字符串，在字符串后面加上，这样字符串就变多了

name = input(prompt)
print(name)                        #前面的相当于一个小提示，把提示和下面的当做一个部分来输出，这样可以节省变量

