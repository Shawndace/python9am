# class Introduction:
#
#     x = 10
#
#     def add(self, x, y):
#         print(x + y)
#
# obj = Introduction()
# # print(obj.get())
# obj.add(10,20)

class Introduction:

    def __init__(self):
        print("This is init method")

    def __str__(self):
        return "I am introoo"


obj = Introduction()
print(obj)
