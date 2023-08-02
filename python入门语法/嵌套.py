age = int(input("输入年龄"))
year = int(input("入职年龄"))
grade = int(input("级别"))
if age>=18:
    if age<30:
        if year>2:
            print("可以领取")
        elif grade>3:
            print("可以领取")
        else:
            print("不可以领取")
    else:
        print("不可以领取")
else:
    print("不可以领取")

# 猜数游戏

import random
num = random.randint(1,10)
print("从1-10中猜取数字")
count = 1
while(count<4):
 count=count+1
 guess = int(input())
 if guess<=10:
    if guess>=1:
        if guess <num:
            print("猜小了")
        elif guess >num:
            print("猜大了")
        else:
            print("猜对了")
 else:
    print("数字不在范围内")
