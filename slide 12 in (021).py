#Solve Example at slide 12 in (021)
Values = [1, 2, 1, 3, 4, 6, 5, 6]

for i in range(1, 7):
    count = Values.count(i)
    print(str(i) + ":" + str(count), end="  ")
