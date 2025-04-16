prompt = "Please enter the age: "

active = True 
while active:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print("please enter number:")

    message = int(message)
    if message <3:
        print("free")
    elif 3 <= message < 12:
        print("10 d")
    else:
        print("15 d")
    break


prompt = "\n请输入年龄（输入 'quit' 退出）: "
active = True

while active:
    user_input = input(prompt)
    
    # 用户输入 'quit' 时退出
    if user_input.lower() == 'quit':
        active = False
        print("程序已退出。")
        break
    
    # 尝试将输入转为数字
    try:
        age = int(user_input)
        
        # 根据年龄判断票价
        if age < 3:
            print("票价：免费")
        elif 3 <= age <= 12:
            print("票价：10 美元")
        else:
            print("票价：15 美元")
    
    except ValueError:
        # 输入非数字时提示错误
        print("错误：请输入数字或 'quit' 退出！")