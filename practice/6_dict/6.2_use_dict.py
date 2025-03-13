#修改jianzhi
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}    #涉及到运算，所以，value为数字的时候不可以加''
print(f"The original position is: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position is {alien_0['x_position']}")

#删除键值对 del dict_name['key']
my_dict = {'age':15,'name':'dong'}
print(my_dict)
del my_dict['age']
print(my_dict)

#格式问题 类型相似的
favorite_languages = {
    'alice':'c',
    'bob':'python',
    'cinda':'c++'
    }

#如果打印的键不存在，例如在my_dict中找到'location'
location_value = my_dict.get('location','no location')
print(location_value)
#键location，值location_value 如果在my_dict中没有找到location，那就返回一个默认值'no location'
# 并将他赋给location_value 可以输出打印
# 如果在后面不加入返回默认值，默认返回None