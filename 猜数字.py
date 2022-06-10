a=8
b=int(input("请在1-10猜一个数字"))
while b != a: 
    if b<a:
        print("猜的数字太小了")
    else:
        print("猜的数字太大了")
    b=int(input("请在——猜一个数字"))
if b==a:
    print("可以哦，猜对了！！！")
    
