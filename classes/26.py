n=int(input("enter a no"))
k=2
while(k<=2):
    c=0
    i=2
    while(i<j//2):
        if n%k==0:
            i=2
            c=0
            while(i<k//2):
                if k%i==0:
                c=c+1
                break
            i=i+1
            if c==0:
                print(k,end='')
    k=k+1
           