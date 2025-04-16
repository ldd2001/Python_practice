prompt = "please enter age to get price or quit to end program: "
#不用active也可以
active = True 
while active:
    message = input(prompt)
    if message == 'quit':
        break                     #如果输入了quit，直接退出

    try:                          # 因为不知道用户可能输入什么内容，所以先try一下试试，出了意外的错，可以纠正
        message = int(message)     # 尝试一下：将用户输入的值赋值给message，把message转化为int ，如果是小数，float
        if message < 3:             # 如果转化不了，就转到except，显示值错误
            print("Free!")
        elif 3 <= message <= 12:
            print("10d")
        else:
            print("15d")               
            # break                      放了break 这就变成了一个一次性的程序
    except ValueError:
        print("you should type a number!")
        # break       在这放break，当输入非quit和数字时，程序断掉

   