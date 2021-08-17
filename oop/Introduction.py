# class Introduction:
#     x = 10
#
#     def test(self):
#         return "welcome to oop"
# obj = Introduction()
#
# print(obj.x)
# print(obj.test())

class Introduction:
    def __init__(self):
        pass
        # return "I am introoo"
    def __str__(self):
        return "I am intro"
    def test(self):
        print("Python")
obj = Introduction()
print(obj)
obj.test()

