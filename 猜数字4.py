import random #导入随机模块
import tkinter 
import tkinter.messagebox
import tkinter.simpledialog

base = tkinter.Tk()
# 设置窗口名称
base.title('猜数小游戏')
# 创建画布 设置大小
canvas = tkinter.Canvas(base,width=420,height=210)
canvas.pack()
# 窗口大小锁定
base.resizable(False,False)

varnumber = tkinter.StringVar(base,value='0')
lb = tkinter.Label(base,text="请输入一个整数:")
lb.place(x=30, y=50, width=100, height=20)

# 生成的随机数
numbers = tkinter.IntVar(base, value=0)
# 设置
def config():
    while 1:
        try:
            least = tkinter.simpledialog.askinteger('最小整数', '最小数', initialvalue=1) # 玩家设置最小值，默认1
            break
        except:
            pass
    while 1:
        try:
            most = tkinter.simpledialog.askinteger('最大整数', '最大数', initialvalue=100) # 玩家设置最大值，默认100
            break
        except:
            pass
    # 判断输入的最小值大于最大值
    if least > most:
        tkinter.messagebox.showerror('错误', '请重新正确输入范围值')
        start['state'] = 'disabled'
        return
    else:
        start['state'] = 'normal'
        numbers.set(random.randint(least,most)) # 从玩家设置的范围内取值
        tkinter.messagebox.showerror('提醒', '您设置的是'+str(least)+'-'+str(most)+'之间')

# 开始
def starts():
    '''
    点击开始按钮之后执行
    进行判断有没有设置新的最大小值
    '''
    if numbers.get() == 0: 
        numbers.set(random.randint(1, 100)) # 没设置将默认从1-100之间取
        tkinter.messagebox.showerror('提醒', '默认1-100之间')
    number['state'] = 'normal'  # 释放输入框
    configuration['state'] = 'disabled'  # 锁定设置按钮
    start['state'] = 'disabled'  # 锁定开始按钮
    determine['state'] = 'normal'  # 释放确定按钮

# 确定
def determines():
    b = int(numbers.get())
    c = number.get()
    if c == '':
        tkinter.messagebox.showerror('抱歉', '值不可为空,请重新输入')
        return
    elif c[0] == '0':
        tkinter.messagebox.showerror('抱歉', '0不能开头,请重新输入')
        return
    try:
        a = int(number.get())
    except:
        tkinter.messagebox.showerror('抱歉', '请正确输入')
        return
    if a == b:
        tkinter.messagebox.showinfo('恭喜', '猜对啦')
        number['state'] = 'disabled'
        configuration['state'] = 'normal'
        determine['state'] = 'disabled'
        start['state'] = 'normal'
    else:
        if a > b:
            tkinter.messagebox.showerror('抱歉', '大')
        elif a < b:
            tkinter.messagebox.showerror('抱歉', '小')

# 数字输入框
number = tkinter.Entry(base, width=100,textvariable=varnumber )
number.place(x=130, y=50, width=100, height=20)
number['state'] = 'disabled' # 设置点击开始之前不可输入

# 开始
start = tkinter.Button(base,text='开始',padx=45,pady=15,command=starts)
start.place(x=205,y=120)

# 设置
configuration = tkinter.Button(base,text='设置',padx=45,pady=15,command=config)
configuration.place(x=65,y=120)
configuration['state'] = 'normal'

# 确定
determine = tkinter.Button(base,text='确定',padx=45,pady=15,command=determines)
determine.place(x=240, y=49, width=100, height=22)
determine['state'] = 'disabled' # 开始游戏之前不可点击
# 进入消息循环
base.mainloop()
