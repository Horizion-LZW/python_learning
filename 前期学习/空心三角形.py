#10层空心三角形
for i in range(1, 11):
    spaces1 = " " * (10 - i)
    if i == 1:
        stars1 = "*"
    elif i == 10:
        stars1 = "*" * 19
    else:
        stars1 = "*" + " " * (2 * i - 3) + "*"
    print(spaces1 + stars1)


