from menu import show_menu
from user import User
from user_managment import UserManager
from admin_login import Admin

def main():
    # admin_username, admin_pin_cod = admin_login()
    admin = Admin()
    if admin.logged_in:
        print(admin.username)
    else:
        print('Admin is not loggedin. Buy!')
        exit() # exit the program

    user_managment = UserManager()
    user = User()

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            user_managment.list_users()
        elif choice == 2:
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            address = input("Enter address: ")
            username = input("Enter username: ")
            pin_code = input("Enter pin code: ")
            user_managment.add_user(name, surname, dob, address, username, pin_code)
        elif choice == 3:
            username = input("Enter username to delete: ")
            user_managment.delete_user(username)
        elif choice == 4:
            username = input("Enter username to show: ")
            user_managment.show_user(username)
        elif choice == 5:
            user_managment.save_users()
            print("Database saved successfully.")
        elif choice == 6:
            print("More options are not implemented yet.")
        elif choice == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()