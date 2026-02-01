n=int(input("Enter anumber:"))
k=n
sum=0
while(n>0):
    dig=n%10
    sum=sum+dig*dig*dig
    n=n//10
    if(sum==n):
        print(n,"is an armstrong no")
    else:
        print(n,"is not a armstrong no")