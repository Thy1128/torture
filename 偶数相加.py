i = 0
sum = 0 
while i <= 10: 
    if i % 2 == 0:
        print(i)
        sum = sum + i 
    i+=1 
print("1-10 的偶数累加和为:%d" % sum) 
