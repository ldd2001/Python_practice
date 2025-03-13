location = ['beijing','shenyang','changsha','hongkong','shanghai']

#打印原始列表
print(f"The origin list is:\n{location}\n")

#使用sorted打印,验证原始列表未变化
print(f"The sorted list is:\n{sorted(location)}\n")
print(f"The origin list is:\n{location}\n")

#使用sorted打印相反列表，无需修改，并再次打印证明顺序未变
print(f"The sorted list is:\n{sorted(location,reverse=True)}")
print(f"The origin list is:\n{location}\n")

#使用reverse()翻转列表并打印，证明顺序变了
location.reverse()
print(f"The reverse list is:\n{location}\n")
print(f"The origin list is:\n{location}\n")

#使用reverse()再次翻转列表并打印，证明顺序变了
location.reverse()
print(f"The reverse list is:\n{location}\n")
print(f"The origin list is:\n{location}\n")

#使用sort修改列表顺序，并验证
location.sort()
print(f"The sort list is:\n{location}\n")
print(f"The origin list is:\n{location}\n")

#移除列表中的hongkong元素,用remove移除后，列表中不再有该元素
location.remove('hongkong')
print(f"The origin list is:\n{location}\n")


# 例如 insert append del sort reverse remove 这种改变列表原始顺序的需要提出单拿出来写一行，例如 name.insert(0,"元素")，list_name.sort()
# sorted这种不改变顺序的，只是临时弄，可以不直接加入，

print(f"Here is the origin text:\n{sorted(location,reverse=True)}")