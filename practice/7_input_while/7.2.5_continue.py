current_number = 0
while current_number < 10:
    current_number += 1
    if current_number %2 == 0:
        continue                 #continue 的作用是如果if语句是真的，那么忽略剩下的代码，返回到while循环的开头
    else:
        print(current_number)
