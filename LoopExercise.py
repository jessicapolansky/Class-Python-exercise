#Exercise 1. 1 to 10
for i in range(1, 11):
    print(i)
    
#Exercise 2. n to m
starter = int(input("Where should I start?: "))
finisher = int(input("When should I end?: "))
for i in range(starter, finisher + 1):
    print(i)
    
#Exercise 3. Odd Numbers
for i in range(1, 10, 2):
    print(i)
    
#Exercise 4. Print a Square
for i in range(1,6):
    print("*" * 5)
    
#Exercise 5. Print a Square II
rows = int(input("How many rows do you need?  "))
stars = int(input("How many stars in each row?  "))
for i in range(1, rows + 1):
    print("*" * stars)
    
#Exercise 6. Print a box
width = int(input("How wide is your box?  "))
height = int(input("How tall is your box?  "))
print("*" * width)
for i in range(1, height - 1):
    print("*" + " " * (width - 2) + "*")
print("*" * width)

#Exercise 7. Print a Triangle
for i in range(0, 4):
    spaces = 4 - i - 1
    stars = i * 2 + 1
    print(' ' * spaces + "*" * stars)
    
#Exercise 8. Print a Triangle II
triangle = int(input("How tall should the triangle be?  "))
for i in range(0, triangle):
    spaces = triangle - i - 1
    stars = i * 2 + 1
    print(' ' * spaces + "*" * stars)
    
#Exercise 9. Multiplication table.
for i in range (1, 11):
    for j in range (1, 11):
        newNum = i * j
        print("{} X {} = {}.".format(i, j, newNum))

#Bonus. Print a Banner
banner = input("What should I print on the banner?  ")
width = len(banner)
print("*" * (width + 4))
print("* " + banner + " *")
print("*" * (width + 4))

#Bonus. Triangle Numbers
tNumbers = []
for i in range(1,101):
    x = (i * (i + 1) / 2)
    tNumbers.append(int(x))
print(tNumbers)

#Bonus. Factor a Number
x = int(input("Give me a number, and I'll tell you its factors: "))
factorList = []
for i in range(1, x + 1):
    if x % i == 0:
        factorList.append(i)
print(factorList)
    
    
