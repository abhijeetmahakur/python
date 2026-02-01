j=10
while(j<=20):
    c=0
    i=2
    while(i<j//2):
        if j%i==0:
         c=c+1
        break
        i=i+1
        
    if c==0:
        print(j,end='')
        j=j+1
           