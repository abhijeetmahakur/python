n=int(input("enter a numkber"))
k=n
sum=0
while(n>0):
    dig=n%10
    fact=1
    i=1
    while(i<=dig):
     fact=fact*i
     i=i+1
     sum=sum+fact
     n=n//10
     sum==k
     print(k,"is a strong no")
    else:
       print(k,"is not a strong no")



