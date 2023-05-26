import random
#随机生成一个数，让用户猜，猜对了，提示猜对了，猜错了，提示猜大了或者猜小了
#输入用户猜数是猜1-10还是1-100
a=int(input("猜数上限是10还是100？"))
if a==10:
    num = random.randint(1,10)
    n=3#1-10的数，最多猜3次
    i = 1
elif a==100:
    num = random.randint(1,100)
    n=10#1-100的数，最多猜10次
else:print("输入错误")#输入错误，直接退出
i=1
while i<=n:
    guess = int(input("请输入你猜的数："))
    if guess == num:
        print("恭喜你，猜对了")
        break#猜对了，直接退出
    elif guess > num:
        print("猜大了")
    elif guess < num:
        print("猜小了")
    i+=1
    if i<=n:
        print("你还有",n-i+1,"次机会")
    else:
        print("你的机会用完了")
        print("正确答案是：",num)#猜错了，输出正确答案