x = int(input())
if x % 4 == 0 and x % 100 == 0 and x % 400 != 0:
    print("平年")
elif x % 4 == 0 or x % 400 == 0:
    print("闰年")