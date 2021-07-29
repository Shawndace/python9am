count = 1
num = int(input("Enter a number: "))
even = 0
odd = 0
while count <= num:
    if count % 2 == 0:
        # print("number is Even")
        even += 1
    else:
        # print("Number is odd")
        odd += 1
    count += 1
print(f"Total even num:{even}")
print(f"total odd num: {odd}")
