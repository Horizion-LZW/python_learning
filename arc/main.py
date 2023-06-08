list1 = [[2.3, 5.4], [9.4, 6.2], [1.2, 9.3],[2.5, 5.7],[9.2, 6.5]]
dict1 = {}
for i in range(1, 11):
    for j in range(1, 11):
        dict1[i, j] = 0

for x in list1:
    row = int(x[0])
    col = int(x[1])
    dict1[row, col] += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(dict1[i, j], end=' ')
    print()
