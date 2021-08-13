print("----Ring Road Bus fare service----")
print("Please select options: ")
print("1.Kalanki-swayambhu\n2.Swayambhu to Gongabu\n3.Gongabu to kalanki")
charge1 = 0

option1 = int(input("Please enter your path: "))
if option1 == 1:
      charge1 += 15
elif option1 == 2:
      charge1 += 15
elif option1 == 3:
      charge1 += 15
else:
      print("No route")
      exit()
