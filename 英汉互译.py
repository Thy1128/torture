from urllib import request
import urllib
import re
from tkinter import *
mygui = Tk(className="趣味翻译")
mygui.geometry('1000x500+200+200')#设置窗口大小及位置
mygui.config(bg="#8DB6CD")

header = {
'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36'}

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
def hit_me():
    form_date = {'i': e.get(),
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15609295378881',
    'sign': '1df1a958a9786081377324bce340e0da',
    'ts': '1560929537888',
    'bv': '8d165ec21fcdbdde58f225cd72fd33e4',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'}

    data = urllib.parse.urlencode(form_date).encode(encoding = 'utf-8')

    req = request.Request(url,headers=header,data=data )

    reponse = request.urlopen(req).read().decode()

    patt = r'"tgt":"(.*?)"}]]}'
    result = re.findall(patt,reponse)#搜索所有满足条件的字符串
    h = StringVar()
    fy = Entry(mygui, textvariable=h, font=('Arial', 20))
    h.set(result[0])
    fy.place(x=800, y=350, anchor=CENTER)

hb=Canvas(mygui,width=200, height=150,bg="white")#创建画布
hb.pack()
#cat = PhotoImage(file="cat.png")  # 打开一张图片
#hb.create_image(100, 75, image=cat)  # 绘制图片
#,bg="#8DB6CD"
while True:
    l0=Label(mygui,text="翻译软件",font=("黑体",20))#书写标签
    l0.place(x=500,y=200,anchor=CENTER)
    l1 = Label(mygui, text="请输入您想翻译的中文或英文:",font=("黑体",20))
    l1.config(cursor="gumby")#鼠标移动样式
    l1.place(x=300, y=300, anchor=CENTER)
    l2 = Label(mygui, text="翻译区：",font=("黑体",20))
    l2.place(x=700, y=300, anchor=CENTER)
    e = StringVar()
    word = Entry(mygui, textvariable=e, font=('Arial', 20))
    e.set('input your text here')
    word.place(x=300, y=350, anchor=CENTER)
    start = Button(mygui, text="开始翻译", command=hit_me,font=('Arial', 20))
    start.place(x=300, y=400, anchor=CENTER)
    mainloop()
