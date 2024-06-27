def add_user(users):
    name = input("Enter the user's name: ")
    dob = input("Enter the user's date of birth (YYYY-MM-DD): ")
    address = input("Enter the user's address: ")
    user_id = len(users) + 1
    users[user_id] = {'name': name, 'date_of_birth': dob, 'address': address}
    print(f"User {name} added successfully!")