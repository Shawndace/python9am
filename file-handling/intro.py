# handle = open('record.txt', 'r')
# handle.write('We are learning file handling......')
# handle.close()

# fs = open('record.txt', 'r')
#
# # print(fs.read())
# # print(fs.readlines())
# print(fs.readline())

file = open('record.txt', 'a')
name = input("Enter your name: ")

file.write(name)
file.write('\n')

file.close()