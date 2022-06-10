def JT():
    a=int(input("请输入鸡和兔的总数："))
    b=int(input("请输入鸡和兔脚的总数："))
    for i in range(1,a):
        if b==i*2+(a-i)*4:
            print("鸡有%d只，兔子有%d只"%(i,a-i))
            break
        if i==a-1:
            print("您输入的总头数和总脚数有误，请重新输入：")
            JT()
JT()
    
