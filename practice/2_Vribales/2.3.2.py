first_name = " 'liilesqrilrq' '"
last_name = " zhao "
fullname = f"{last_name},{first_name}" #f"",不加f，变量fullname只是一句话
                                       #            加了f，不仅可以输出字符串，把字符串加入{}可以打印变量的值
print(fullname)                        #直接打印变量fullname的内容
print("hello,{fullname}")              #没加f,会直接打印出""的内容，变量fullname并没有打印出来
print(f"hello,{fullname}")             #加了f之后，变量fullname的值会被打印出来
print(f"hello,{fullname.title()}")     #在字符串变量名后加入.title()，会打印出大小写
#可以进行变量套变量，例如
message = f"hello,{fullname.title()}"  #f""中间可以加入其他字符串，.title()可以加在任意变量后，输出时用
print(message)

#制表符\t 换行符\n  制表符只是让内容向后退，不能实现换行
print(f"\thello,{fullname.title()}")  
print("\thello")
print("it\n\tis\tme\n")

#str.rstrip(),给定字符串，创建一个副本，不改变原变量 全部删除
ma = f"{first_name.rstrip()}"
print(ma)
