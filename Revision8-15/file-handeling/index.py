import getpass
import os

if not os.path.exists('record.txt'):
    file = open('record.txt', 'w')



def register():
    print("--- Register user ---")
    username = input("Enter username: ")
    if username in open('record.txt', 'r').read():
        print("Username already exists !")
        exit()
    password = getpass.getpass("Enter password: ")
    confPassword = getpass.getpass("confirm password: ")
    if password != confPassword:
        print("password does not match! ")
        exit()
    file = open('record.txt', 'a')
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    print("Successfully registered!!")
    exit()

def login():
    print("--- Login page ---")
    username = input("enter username: ")
    password = getpass.getpass("enter password: ")
    get_record = open('record.txt', 'r')
    # removed readlines here in get_record
    all_user = []
    counter = 0
    login_success = False

    for users in get_record:
        all_user.append(users.split())
    # print(all_user)

    tot_users = len(all_user)
    while counter < tot_users:
        uname = all_user[counter][0]
        pwd = all_user[counter][1]
        if uname == username and pwd == password:
            print("Aijo")
            exit()
            # login_success = True
        else:
            print("bhakkk")
            exit()
        counter += 1
    # if login_success == True:
    #     print("Welcome!")
    # else:
    #     print("Bhak")

question = input("Do you have account? y/n?")
if question == 'y':
    login()
elif question == 'n':
    register()
else:
    print("Invalid options!")
    exit()




