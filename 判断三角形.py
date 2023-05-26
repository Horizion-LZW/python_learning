#输入三个数，判断能否组成三角形，如能，判断三角形类型
# 1.等边三角形 2.等腰三角形 3.一般三角形 4.直角三角形 5.不能构成三角形
#a = int(input("请输入第一个数："))
#b = int(input("请输入第二个数："))
#c = int(input("请输入第三个数："))
a,b,c =map(int,input('输入三条边a,b,c并用空格隔开:').split())#在此处尝试了一下对三个数进行连续输入
if a+b>c and a+c>b and b+c>a:
    #在满足三角形条件的情况下，判断三角形类型
    if a == b == c:
        print("等边三角形")
    elif a == b or a == c or b == c:
        print("等腰三角形")
    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        print("直角三角形")
    else:
        print("一般三角形")
else:#不满足三角形条件
    print("不能构成三角形")


