import os
import getpass

if not os.path.exists('userinfo.txt'):
    fc = open('userinfo.txt','w')
    fc.close()

def register():
    username = input("Enter username: ")
    if username in open('userinfo.txt','r').read():
        print("Username already exists!! ")
        exit()
    password = getpass.getpass("Enter password: ")
    conf_pass = getpass.getpass("Confirm password: ")
    if password != conf_pass:
        print("Password doesnot match try again!!")
        exit()

    file = open('userinfo.txt','a')
    file.write(username)
    file.write(' ')
    file.write(password)
    file.write('\n')
    print('user created succesfully! ')
    file.close()
    exit()

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    get_record = open('userinfo.txt','r').readlines()
    all_user = []

    for user in get_record:
        all_user.append(user.split())

    total_user = len(all_user)
    increment = 0
    login_success = False
    while increment < total_user:
        uname = all_user[increment][0]
        pwd = all_user[increment][1]
        if uname == username and password == pwd:
            login_success = True
        increment += 1

    if login_success == True:
        print(f"Welcome: {username}")
    else:
        print("Credentials not match!")


question = input("Do you have an account? (y/n):  ")
if question == 'y':
    login()
elif question == 'n':
    register()
else:
    print("Invalid")
