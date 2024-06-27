def view_user(users, user_id):
    if user_id in users:
        user = users[user_id]
        print(f"Name: {user['name']}\nDate of Birth: {user['date_of_birth']}\nAddress: {user['address']}")
    else:
        print("User not found.")