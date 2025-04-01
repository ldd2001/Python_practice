#在字典中存列表 ； 一个key关联多个value时

favorite_languages = {
    'jen':['python','c++'],
    'sarah':['c'],
    'edward':['rust','fortan'],
    'phile':['c','c++']
}

for name, languages in favorite_languages.items():            # key values 一定要对应字典
    if len(languages) > 1:
        print(f"{name.title()}'s favorite languages are:")        #  
        for language in languages:                                # 对应list
            print(f"{language.title()}")
    else:
        print(f"{name.title()}'s favorite languages is:")        #  
        for language in languages:                                # 对应list
            print(f"{language.title()}")

            
#想想为什么下面的代码不对
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in favorite_languages.values():   #问题出在这：。title用于字符串，favorite_langues.values他是一个列表，是不可以用.title的
        print(f"{language.title()}")               #所以，for name languages里面，language就是列表，所以，13行，就是从列表里提取字符串