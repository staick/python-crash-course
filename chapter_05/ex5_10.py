current_users = ['root', 'staick', 'anyone', 'jack', 'admin']
new_users = ['Mary', 'john', 'json', 'root', 'jack']

for user in new_users:
    if user.lower() in current_users:
        print(f'The name {user} is occupied, please try another one.')
    else:
        print('Great! You can use this user name.')

# 创建小写副本？
