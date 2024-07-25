import os


class User:
    def __init__(self, name, surname, dob, address, username, pin_code):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.address = address
        self.username = username
        self.pin_code = pin_code

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.dob}, {self.address}, {self.username}, {self.pin_code}'

class UserManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.users = []

    def load_users(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 6:
                        self.users.append(User(*data))


# Assuming the User and UserManager classes are defined above or imported

if __name__ == "__main__":
    # Create an instance of UserManager with the path to the test file
    manager = UserManager('users_db.txt')
    
    # Call the load_users method
    manager.load_users()
    
    # Print the loaded users to verify
    for user in manager.users:
        print(user)


