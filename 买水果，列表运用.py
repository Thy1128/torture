fruits=["苹果","香蕉","橘子","荔枝"]
while True:
    a=int(input("输入0退出程序，输入1选水果\n"))
    if a ==1:
        fruit=input("请输入你想吃的水果\n")
        if fruit in fruits:
            print("你以获取当前水果，请享用")
        else:
            fruits.append(fruit)
            print("暂时没有你想要的水果，正在采购，下次再来")
    else:
        print("欢迎下次光临！！！")
        break
