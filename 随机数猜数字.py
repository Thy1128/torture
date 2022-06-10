import random  
a = random.randint(1,10)   
b = int(input("请在1-10之间输入一个数："))
while b!=a :
    if b<a:
        print("数字猜小了")
    else:
        print("数字猜大了")
    b = int(input("请在1-10之间输入一个数："))
if a == b:
    print("ok,被你猜中了！！！")
    
