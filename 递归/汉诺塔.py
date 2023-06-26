# 汉诺塔问题
cout = 1


def han(n, a, b, c):
    global count
    if n == 1:
        print(count, a, '-->', c)
        count += 1
    else:
        han(n - 1, a, c, b)
        han(1, a, b, c)
        han(n - 1, b, a, c)
    return 'over'


print(han(64, "X", "Y", "Z"))
