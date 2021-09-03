# def add(x, y):
#     return f"the sum is: {x + y}"
#
# def sub(x, y):
#     return f"the subtraction is: {x - y}"
#
# def mul(x, y):
#     return f"the muliply is: {x * y}"
#
# def div(x, y):
#     return f"the division is: {x / y}"
#
# sum = add(5,5)
#
# print(sum)
#
# print(sub(10,10))
# print(mul(10,10))
# print(div(10,10))

# using anonymous function------------------------


x = lambda a, b : a + b
print(f"sum is: {x(2,3)}")

y = lambda a, b : a - b
print(f"sub is: {y(5,2)}")

z= lambda a,b : a * b
print(f"multiplication is: {z(2,2)}")