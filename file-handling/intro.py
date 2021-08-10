# handle = open('record.txt', 'a')
# handle.write("Hey this is python")
# handle.write("This is python okayyy")
#
# obj = open('studentName.txt', 'w')
# obj.write("Am learning pythonn")
# handle.close()
# obj.close()
#
# obj = open('record.txt', 'r')
# print(obj.readlines())
# # print(obj.readline())
# # print(obj.read())

file = open('record.txt', 'a')
username = int(input("Enter your name: "))
file.write(f"{username}")
file.write('\n')

file.close()