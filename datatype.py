# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# phone = input("Enter your number: ")
# print("Your name is " + name + " and you are " + age + "years old" + " your number is: " + phone)
#
# name = input("Enter your name: ")
# age = float(input("Enter your age: "))
# phone = int(input("Enter your number: "))
#
# print(f"my name is {name}, I'm  {age} years old and my number is {phone}")

# principal = float(input("Enter principal: "))
# time = float(input("Enter time: "))
# rate = float(input("Enter the rate: "))
#
# print((principal * time * rate)/100)
#
# print(f"Your intrest rate is: {(principal*time*rate)/100}")

# name = last_name = 'Sandesh'
# print(name)
# print(last_name)

# x = input("enter a number: ")
# print(x)

# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
# print(x + y)
#
# x = input("Enter first number: ")
# y = input("Enter second number: ")
# x = int(x)
# y = int(y)
#
# print(x + y)

# x, y = input("Enter x,y: ").split(',')
#
# print(x, y)

# name = input("Enter client's name: ")
# age = int(input("Enter client's age: "))
# phoneNumber = int(input("Enter client's number: "))
#
# print(f"your client's name is {name}, he is {age} years old and his phone number is {phoneNumber}")
# print("This is pything")


# x = 10j
# print(type(x))

# x = 23.334567
# name = 'Sandesh'
# print('{:.2f}'.format(x))
# print('{:.2}'.format(name))

# x = 2 + 3i
#
# print(x.real)
# print(x.imag)

# Python code to demonstrate the working of
# complex(), real() and imag()

# importing "cmath" for complex number operations
# import cmath

# https://www.geeksforgeeks.org/complex-numbers-in-python-set-1-introduction/
# Initializing real numbers
# x = 5
# y = 3
#
# converting x and y into complex number
# z = complex(x,y);
#
# printing real and imaginary part of complex number
# print ("The real part of complex number is : ",end="")
# print (z.real)
#
# print ("The imaginary part of complex number is : ",end="")
# print (z.imag)
#
#
# # Python code to demonstrate the working of
# # phase()
#
# # importing "cmath" for complex number operations
# import cmath
#
# # Initializing real numbers
# x = -1.0
# y = 0.0
#
# converting x and y into complex number
# z = complex(x,y);
#
# printing phase of a complex number using phase()
# print ("The phase of complex number is : ",end="")
# print (cmath.phase(z))

# ----------------------------------------------
# DAY4
# LIST[] - mutable

# data = ['Ram', 123, 'Hari']
# print(data)
# print(data[0])
# data[0]='San'
# print(data)

# numbers = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, [14, 15]]
# ]
#
# print(numbers[2][3][1])

# --------------------------------------

# tuple () - inmutable

# tuple1 = (1, 2, 3)
# tuple2 = 1, 2, 3
# print(type(tuple1))
# print(tuple2)

# ------------------------------------------
# set {} - no unique element in output

# data = {1, 2, 3, 1}
# print(data)

# ------------------------------------------------
# dic{'':''} - key value pair

# data = {'Name': 'Sandesh', 'Age': 24}
# print(data['Name'])
#
# data = [
#     {'name': 'Ram'},
#     {'name': 'Sita', 'age':25}
# ]
# print(f"name is {data[1]['name']}, her age is {data[1]['age']}")
# print(data[1]['name'],['age'])

# data = [
#     {'name': 'Sita', 'age': 34},
#     {'name2': 'Hari', 'age2': 35}
# ]
# print(f"Her name is {data[0]['name']} and her age is{data[0]['age']}")
