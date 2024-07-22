class Admin:
    def __init__(self) -> None:
        self.admin_login()

    def admin_login(self):
        print("Administrator Login")
        self.username = input("Enter your username: ")
        self.pin_code = input("Enter your pin_code: ")
        self.logged_in = False

        if self.username == "admin" and self.pin_code == "1329":  # Example username and pin code
            print("\nHello! Welcome, to the user management system!")
            self.logged_in = True
        else:
            print("Invalid username or pin code. Please try again.")

# Create an instance of Admin to test
admin_instance = Admin()



      