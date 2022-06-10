import time
date=time.strftime('%Y-%m-%d')
print("Today is:",date)
def writeNote():
    print("please input your diary,if you want to stop,please input the order:'end'")
    fd=open(date,'a')
    while True:
        line=input()
        if line=='end':
            break
        fd.write(line+'\n')
    fd.close()
writeNote()
