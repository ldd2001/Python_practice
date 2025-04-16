prompt = "tell...."
prompt += "enter 'quit' to end program"
#核心是让程序按照active的值来运行，
active = True 
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
    
