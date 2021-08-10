import os
import getpass

if not os.path.exists('database.txt'):
    fs = open('database.txt', 'w')
    fs.close()


def register():
    print("----- Create a new user ------")
    username = input("Enter a username: ")
    if username in open('database.txt', 'r').read():
        print("Username already exist!")
        exit()
    password = getpass.getpass("Enter a password: ")
    confirm_pass = getpass.getpass("COnfirm your password: ")
    if password != confirm_pass:
        print("Password not match! ")
        exit()
    file = open("database.txt", 'a')
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write('\n')
    file.close()
    print("User succefully created !! ")
    exit()


def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    get_record = open('database.txt', 'r').readlines()
    all_users = []
    for user in get_record:
        all_users.append(user.split())

    total_users = len(all_users)
    increment = 0
    login_success = False
    while increment < total_users:
        uname = all_users[increment][0]
        upass = all_users[increment][1]
        if username == uname and password == upass:
            login_success = True
        increment += 1
    if login_success == True:
        print(f"Welcome {username}")
    else:
        print("username or password not correct! ")

question = input("Do you have an account? y/n ?")
if question == 'y':
    login()
else:
    register()
