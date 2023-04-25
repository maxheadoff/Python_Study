row = 3
column = 5

A = []

'''
for i in range(row):
    for j in range(column):
        B = [int(input("введите число:"))]
    A.append(B)
'''

A.append([1, 2, 3, 4, 5])

A.append([10, 10, 10, 10, 10])
A.append([1, 2, 3, 4, 5])

for i in range(row):
    print(A[i])


sumGlobal = 0

for i in range(row):
    sum = 0
    for j in range(column):
        sum += A[i][j]
    sumGlobal += sum
    A[i].append(sum)
    print("строка {}, сумма:{}".format(i,sum))

for i in range(row):
    print(A[i])

stepSum = 0
maxIndex = 0
for i in range(row):
    if stepSum < A[i][column]:
        stepSum = A[i][column]
        maxIndex = i
print ("Индекс строки с наибольшей суммой:{}, Сумма:{}".format(maxIndex, stepSum))

print("Общая сумма:{}".format(sumGlobal))

maxIndex = 0
stepSum = 0
for i in range(row):
    sum = 0
    for j in range(column):
        sum += A[i][j]
    if stepSum < sum:
        stepSum = sum
        maxIndex = i
    sumGlobal += sum
    print("строка {}, сумма:{}".format(i,sum))
print ("Индекс строки с наибольшей суммой:{}, Сумма:{}".format(maxIndex, stepSum))