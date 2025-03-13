#嵌套 列表套字典，字典套列表，字典套字典
alien_0 = {'color':'green','speed':"slow",'points':5}
alien_1 = {'color':'yellow','speed':"slow",'points':10}
alien_2 = {'color':'red','speed':"slow",'points':15}

aliens = [alien_0, alien_1, alien_2]                  #在列表里面嵌套字典 把字典加入列表中

for alien in aliens:
    print(alien)

#有时候需要创建多个列表，

aliens_0 = []     #创建放置外星人的列表
for alien_number in range(30):               #循环生成30次
    new_alien = {'color':'yellow','speed':"slow",'points':10}
    aliens_0.append(new_alien)               #aliens_0是一个列表，newalien 是一个字典，将字典套入alien

for alien in aliens_0[0:5]:
    print(alien)
print('...')

aliens_1 = []
for alien_number_1 in range(5):
    new_alien_1 = {'color':'yellow','speed':"slow",'points':10}
    new_alien_2 = {'color':'green','speed':"fast",'points':5}
    aliens_1.append(new_alien_1)
    aliens_1.append(new_alien_2)
    


