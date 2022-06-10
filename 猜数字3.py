'''
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
'''

import tkinter as tk
import random
from tkinter import messagebox

win = tk.Tk()
# 设置主窗口
win.geometry('400x300')
win.title("C语言中文网")
win.resizable(0,0)
# 创建输入框控件
entry1 = tk.Entry(win)
# 放置输入框，并设置位置
entry1.pack(padx = 20, pady = 20)

# 得到输入框字符串
print(entry1.get())
# 删除所有字符
# entry1.delete(0, tk.END)
# 当按钮被点击的时候执行click_button()函数
def click_button():
    # 使用消息对话框控件，showinfo()表示温馨提示
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
    messagebox.showinfo(title='温馨提示', message='欢迎使用tk库')

# 点击按钮时执行的函数
button = tk.Button(win, text='提交', bg='#7CCD7C', width=20, height=5, command=click_button).pack()

win.mainloop()