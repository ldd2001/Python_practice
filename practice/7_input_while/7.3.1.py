unconfirmed_users = ['Alice','bob','cindy']
confirmed_users = []

#将未验证的全部添加到已经验证

while unconfirmed_users:     
    current_users = unconfirmed_users.pop()               # 从未验证的列表中最后一位
    print("Verifying user: " + current_users.title())
    confirmed_users.append(current_users)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user)

# while unconfirmed_users:
# while 用True 和False 进行判断，非空容器布尔值为True，while就可以进行循环
# while unconfirmed_users 等价于 while len(unconfirmed_users) > 0