current_users = ['eric', 'aleks', 'admin', 'evelin', 'Vladko']
new_users = ['Toma', 'Aleks', 'George', 'vladko', 'Maria']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")
