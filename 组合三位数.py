for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print (i,j,k)
print("===========================================================")
q = 0
while q < 4:
    q+=1
    w = 0
    while w < 4:
        w+=1
        e = 0
        while e < 4:
            e+=1
            if(q != e) and (q != w) and (w != e):
                print(q,w,e)