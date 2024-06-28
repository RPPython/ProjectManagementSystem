users_db = [
    {
        'name': 'Svetlin',
        'surname': 'Sofroniev',
        'date_of_birth' : '14/1/1976',
        'address' : 'Sofia, Str. Pleven 6',
        'username' : 'ss' ,
        'pin_code' : '0001'
        
    },
    {
        'name': 'Mariya',
        'surname': 'Mersinkova',
        'date_of_birth' : '15/9/1970',
        'address' : 'Shumen,Str. Nancho Popovich 35a',
        'username' : 'mm' ,
        'pin_code' : '0002'
        
    },
    {
        'name': 'Pavel',
        'surname': 'Zlatanov',
        'date_of_birth' : '20/5/1993',
        'address' : 'Sofia, Str. Usmivka 2',
        'username' : "pz",
        'pin_code' : '0003'
        
    }
]

def get_user_by_key(key, value):
    filtered_user = [user for user in users_db if user[key] == value]
    if filtered_user:
        return filtered_user[0]
    else:
        print(f'No user with {key}={value}')


if __name__=="__main__":
    username = input("Enter username of the user to view data: ")
    user = get_user_by_key(key='username', value=username)
    print(user)

