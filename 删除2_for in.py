#删除列表中所有的2
li1=[1,2,3,1,2,3,1,2,3,4,2,5,2,5]
for i in li1:
    if i==2:
        li1.remove(i)
print(li1)