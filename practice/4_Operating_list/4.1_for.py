#for循环，对于列表 magicians 中的每个 magician ，都打印他们的名字，列表有多少个元素就循环多少次

magicians = ['alice','david','carolina']
for magician in magicians:                         #for循环一定要加:
    print(f"The name of magician is {magician}")   #变量名称可以随便取，但尽量保持和列表名称相同，列表名称为复数，元素变量名为单数
    print(f"We hope your show {magician} again!")  #for循环，执行缩进的全部语句为一次循环

print("Hello,world")   #对于不在for循环缩进的句子，for循环不起作用                            