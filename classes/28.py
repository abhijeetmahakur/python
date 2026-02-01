n=int(input("Enter the number:"))
k=n
c=0
while n>0:
    if n&1==1:
        c=c+1
    n=n>>1
print("no 1's in",k,"is:",c)