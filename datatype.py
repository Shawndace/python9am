
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

data = [
    {'name': 'Sita', 'age': 34},
    {'name2': 'Hari', 'age2': 35}
]
print(f"Her name is {data[0]['name']} and her age is{data[0]['age']}")
