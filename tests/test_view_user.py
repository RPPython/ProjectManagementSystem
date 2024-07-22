from data import data_handler
from data_handler import users_db
from users_db import get_user_by_key


def view_user(user):
    if user:
        print(f"Name: {user['name']}\nSurname: {user['surname']}\nDate of Birth: {user['date_of_birth']}\n"
              f"Address: {user['address_street']} {user['address_number']}, {user['address_city']}\n"
              f"PIN Code: {user['pin_code']}\nUsername: {user['username']}")
    else:
        print("User not found.")

if __name__=='__main__':
    username = input("Enter username of the user to view data: ")
    user = get_user_by_key(key='username', value=username)
    view_user(user)


