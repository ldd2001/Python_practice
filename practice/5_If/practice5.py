#5.10
current_users = ['Alice','Bob','Cindy','daviD','emIli']
new_users = ['Alice','bob','flander','gates','holid']

# 不区分大小写
new_users_lower = [new_user.lower() for new_user in new_users]
current_users_lower = [current_user.lower() for current_user in current_users]

for new_user_lower in new_users_lower:
    if new_user_lower in current_users_lower:
        print(f"you can't use '{new_user_lower}', beacuse someone has used this name.")
    else:
        print(f"you can use this name")

