#Exercise 1. Sum the Numbers
numbers1 = [1, 3, 5, 7, 9]
print(sum(numbers1))

#Exercise 2. Largest Number
numbers2 = [1, 100, 5, 17, 9]
numbers2.sort()
print(numbers2[-1])

#Exercise 3. Smallest Number
numbers3 = [1, 100, 5, 17, 9]
numbers3.sort()
print(numbers3[0])

#Exercise 4. Even Numbers
numbers4 = [2, 3, 6, 5, 13, 20]
x = 0
evenList = []
while x < len(numbers4):
    if numbers4[x] % 2 == 0:
        evenList.append(numbers4[x])
        x += 1
    else:
        x += 1
print(evenList)
        
#Exercise 5. Positive Numbers
numbers5 = [-2, 3, -6, 0, 13, 20]
x = 0
while x < len(numbers5):
    if numbers5[x] > 0:
        print(numbers5[x])
        x += 1
    else:
        x += 1
        
#Exercise 6. Positive Numbers II
numbers6 = [-2, 3, -6, 0, 13, 20]
x = 0
positiveList = []
while x < len(numbers6):
    if numbers6[x] > 0:
        positiveList.append(numbers6[x])
        x += 1
    else:
        x += 1
print("The positive numbers are: {}.".format(positiveList))

#Exercise 7. Multiply a list
numbers7 = [-2, 3, -6, 0, 13, 20]
enhancedNumbers = [x * 3 for x in numbers7]
print("{} * 3 is {}.".format(numbers7, enhancedNumbers))

#Exercise 8. Multiply Vectors
numbers8a = [-2, 3, -6, 0, 13]
numbers8b = [1, 3, 5, 7, 9]
i = 0
newList = []
while i < len(numbers8a):
    newNum = numbers8a[i] * numbers8b[i]
    newList.append(newNum)
    i += 1
print("{} * {} equals {}.".format(numbers8a, numbers8b, newList))

#Exercise 9. Matrix Addition
matrix9a = [[1, 2], [2, 1]]
matrix9b = [[3, 4], [3, 4]]
res = []
for i in range(len(matrix9a)):
    row = []
    for j in range(len(matrix9a[0])):
        row.append(matrix9a[i][j] + matrix9b[i][j])
    res.append(row)
print(res)

#Exercise 10. Matrix Addition II (same thing, just extended the matrices to show it still works)
matrix10a = [[1, 2], [2, 1], [2, 3]]
matrix10b = [[3, 4], [3, 4], [5, 4]]
res = []
for i in range(len(matrix10a)):
    row = []
    for j in range(len(matrix10a[0])):
        row.append(matrix10a[i][j] + matrix10b[i][j])
    res.append(row)
print(res)

#Exercise 11. De-dup
rawData = [1, 4, 1, 3, 3, 4, 5, 0, 1]
print(list(set(rawData)))

#Bonus
matrixBonusa = [[1, 2], [2, 1]]
matrixBonusb = [[3, 4], [3, 4]]
res = []
for i in range(len(matrixBonusa)):
    row = []
    for j in range(len(matrixBonusa[0])):
        row.append(matrixBonusa[i][j] * matrixBonusb[i][j])
    res.append(row)
print(res)