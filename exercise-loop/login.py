users = [
    ['admin', 'admin1'],
    ['sita', 'sita1'],
    ['gita', 'gita1']
]

print("Enter a user name: ")
userName = input()
print("Enter password: ")
password = input()

total_users = len(users)

# total_users = len(users)
increment = 0
login_success = False
while increment < total_users:
    uname = users[increment][0]
    pws = users[increment][1]
    if uname == userName and pws == password:
        login_success += True
    increment += 1
if login_success == True:
    print("Welcome")
else:
    print("username or password incorrect")
