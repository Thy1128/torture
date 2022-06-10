num = 0
total = 0
name =input("请输入菜名：")
while name !="over":
    price = int(input("请输入价格"))
    num = num+1
    total = total+price
    name =input("请输入菜名：")
print("您一共点了",num,"个菜","总价为：",total,"元")
