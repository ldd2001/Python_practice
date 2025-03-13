#字典 能储存不变的变量以及它的值  dict_name = {'key_1':'value_1','key_2':'value_2'}  key：键 value：值
#注意：''加上去，内部内容为字符串，不可以进行加减，因此，如果后面是数字，可以不用加''
alien_0 = {'color':'green','point':'5'}
print(alien_0['color'])                                  #print(dict_name['key_name']) 就会输出该key的值
print(f"alien_0's point is {alien_0['point']}")

#添加键值对 dict_name['new_key'] = value_new
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#定义空字典 dict_name = {}
alien_1 = {}
alien_1['age'] = 1
print(alien_1['age'])

#修改字典中的·值
alien_1['age'] = '2'
print(alien_1['age'])
