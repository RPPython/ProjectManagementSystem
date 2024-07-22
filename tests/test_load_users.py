import os
from user import User


def load_users(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 6:
                        self.users.append(User(*data))

print(User)
