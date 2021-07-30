# users = ['ram', 'shyam', 'Gita', 'Hari']
#
# # print(users[3])
#
# for name in users:
#     print(name)
#
# users2 = [
#     ['ram', 'shyam', 'Gita', 'Hari'],
#     ['bam', 'chyam', 'Rita', 'MAri'],
#     ['pam', 'jhyam', 'Pita', 'Gari'],
#     ['ham', 'kyam', 'Hita', 'pari'],
#     ['kam', 'ryam', 'Sita', 'chari'],
# ]
#
# for name in users2:
#     for nam in name:
#         print(nam)
#
# for x in range(20):
#     print(x)
#
# x = 1
#
# while x < 10:
#     print(x, end=',')
#     x += 1
#
#
# increment = 1
# num = int(input("Enter a number of time u wanna loop: "))
#
# while increment <= num:
#     if increment == 3:
#         print(increment)
#         break
#
#     increment += 1

users = [
    ['ram', 'shyam', 'bam', 'kam'],
    ['ram', 'shyam', 'bam', 'kam'],
    ['ram', 'shyam', 'bam', 'kam'],
    ['ram', 'shyam', 'bam', 'kam']
        ]

for name in users:
    for showName in name:
        print(showName)
