#列表里面嵌套字典，适合  顺序处理大量相似字典 

aliens = []
#生成5次循环，先生成alien0，在生成alien1 把alien0添加，把alien1添加，各5次循环
for alien_number in range(5):
    new_alien_0 = {'color':'green','points':5}
    new_alien_1 = {'color':'red','points':10}
    aliens.append(new_alien_0)
    aliens.append(new_alien_1)
#打印出所有的外星人
for alien in aliens:
    print(f"{alien}\n")
#修改外星人的颜色 如果外星人是绿色的，修改为yellow
for alien in aliens:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 20
    else:
        alien['color'] = 'origin'
        alien['points'] = 15
#只打印出前五个
for alien in aliens[:5]:
    print(f"{alien}\n")