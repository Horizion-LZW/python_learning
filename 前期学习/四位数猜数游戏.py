import random

# 生成四位不重复数
def generate():
    list = []
    while len(list) < 4:
        num = random.randint(0, 9)
        if num not in list:
            list.append(num)
    return list


# 开始猜数
i = 0

count1 = 0
count2 = 0
list = generate()
while i < 10:
    j = 0
    print("请输入四位数字，还有%d次猜数机会" % (10 - i))
    guess = input()
    num = str(guess)
    if len(num) != 4:
        print("输入错误")
    num_list = [int(j) for j in num]
    for j in range(4):
        if num_list[j] in list and list.index(num_list[j]) == j:
            count1 += 1
        elif num_list[j] in list and list.index(num_list[j]) != j:
            count2 += 1
    if count1 == 4:
        print("恭喜你猜对了")
        break
    else:
        print("%d正%d歪" % (count1, count2))
    i += 1
print("正确数字是：", list)
