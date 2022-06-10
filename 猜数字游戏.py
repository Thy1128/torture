import random
print("************************************************")
print("你好，我们来玩个文字游戏吧，我心中有个数1-30")
print("你一共有五次机会来猜这个数，挑战开始了！！！")
print("************************************************")
times = 0
a = 0
secret = random.randint(1,30)
while secret!=a and times < 5:
    a = int(input("请输入一个数："))
    if a<secret:
        print("你猜的数字小了")
    elif a>secret:
        print("你猜的数字大了")
    times = times + 1
    print("你还有"+ str(5-times) +"次几次")
    
if secret == a:    
    print("你可真机智，恭喜你猜对了！！！")
else:
    print("GAME OVER!!")
 

