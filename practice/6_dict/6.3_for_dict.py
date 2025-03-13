#1. 遍历所有键值对
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
    }
for key, value in user_0.items():    #items()返回键值对列表
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# key，value 可以换成其他的，只是一个变量名而已
for str_0, str_1 in user_0.items():
    print(f"\nkey: {str_0}")
    print(f"value: {str_1}")

#只遍历 键 .keys()  
favorite_languages = {
    'cinda':'c++',
    'bob':'python',
    'emili':'c',
    'david':'go',
    'alice':'c'
    }
friends = ['bob','emili']

for name in favorite_languages.keys():
    print(f"\nName is {name}")

    if name in friends:
        print(f"{name} is my friend")
#检查emili是否被遍历，是的话就输出ok，不是就显示no emili，不要对此进行循环，因此不放在for循环目录下
if 'emili' not in favorite_languages.keys():
    print(f"no emili")
else:
    print("emili is ok")

#按照顺序遍历
for name in sorted(favorite_languages.keys()):  #sorted总是会返回一个新的排序结果，而不改变以前的排序
    print(f"{name.title()}, thank you!")


#打印value 
for value in favorite_languages.values():
    print(value)

# 事实上，value中有很多重复的值，因此如果打印value，就需要去掉重复 采用集合set() 集合是无序的，用来做计算很好
print("\n")
for value in set(favorite_languages.values()):
    print(value)