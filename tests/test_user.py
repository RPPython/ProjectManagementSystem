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


if __name__ == "__main__":
    user1 = User('Svetlin', 'Sofroniev', '14/1/1976', 'Sofia, Str. Pleven 6', 'ss', '0001')
    user2 = User('Mariya', 'Mersinkova', '15/9/1970', 'Shumen, Str. Nancho Popovich 35a', 'mm', '0002')
    user3 = User('Pavel', 'Zlatanov', '20/5/1993', 'Sofia, Str. Usmivka 2', 'pz', '0003')

    print(user1)
    print(user2)
    print(user3)
