def reverse(x):
    b = str(x)
    # 字符串翻转
    i = len(b)
    a = ''
    while i > 0:
        a += b[i - 1]
        i = i - 1
    return a
print(reverse(-123))
