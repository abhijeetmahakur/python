n=int(input("Enter a no:"))
i=1
sum=0
print("factors ofn","are")
while (i<=n):
    if n%i==0:
        sum=sum+i
        i=i+1
        print("sum=",sum)