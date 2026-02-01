for n in range (2,101):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        print(i)



    #or
    for i in range (1,101):
        c=0
        for j in range(2,i//2+1):
            if i%j==0:
                c=c+1
            break
        if c==0:
            print(i,end=" ")
