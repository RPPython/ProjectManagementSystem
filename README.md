***
***
## USER ACCOUNT MANAGEMENT SYSTEM
***
***

## Introduction

The **User Account Management System** is designed to allow administrators to manage user accounts with various functionalities. Administrators can perform tasks such as checking current users, adding new users, deleting users, viewing user data, saving results, and more. The system is built using fundamental constructs such as loops, if conditions, input/output operations, and data structures like lists and dictionaries.


**Login to the system**

The administrator can login to the system by entering their login:

    * username 
    * password


## Features

1. **Check Current Users**: View a list of all current users in the system.
2. **Add New User**: Add a new user by providing their name, date of birth, and address.
3. **Delete User**: Remove a user from the system.
4. **View User Data**: View detailed information of a specific user.
5. **Save Results**: Save the current state of user data.
6. **Additional Options**: Other functionalities as needed.
7. **Exit Program**: Safely exit the program.

## Installation

1. Ensure you have Python installed on your system.
2. Clone this repository or download the project files.
3. Navigate to the project directory.

## Usage

1. Run the `main.py` file to start the application.
2. Follow the on-screen prompts to navigate through the various options available.

### Example Commands

- **Add User**: Input the name, date of birth, and address when prompted.
- **Delete User**: Provide the user's identifier to delete the user.
- **View User Data**: Enter the user's identifier to view their details.
- **Save Results**: Save the current data to a file.

## Code Structure

- `main.py`: The main entry point of the application.
- `user_management.py`: Contains functions for user management operations.
- `data_handler.py`: Handles data input/output operations.

## Data Structures

- **List**: Used to store a collection of users.
- **Dictionary**: Used to store individual user data (e.g., name, date of birth, address).

## Example Code Snippet

```python
# Adding a new user
def add_user(users):
    name = input("Enter the user's name: ")
    dob = input("Enter the user's date of birth (YYYY-MM-DD): ")
    address = input("Enter the user's address: ")
    user_id = len(users) + 1
    users[user_id] = {'name': name, 'date_of_birth': dob, 'address': address}
    print(f"User {name} added successfully!")

# Viewing user data
def view_user(users, user_id):
    if user_id in users:
        user = users[user_id]
        print(f"Name: {user['name']}\nDate of Birth: {user['date_of_birth']}\nAddress: {user['address']}")
    else:
        print("User not found.")
```

## Contributing

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please feel free to reach out.












