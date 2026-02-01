s=5
for i in range(1,s+1):
    for j in range(s,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print( )    