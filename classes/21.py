n=int(input("Enter a no:"))
i=1
sum=0
print("factors ofn","are")
while (i<n):
    if n%i==0:
        sum=sum+i
        i=i+1
        if sum==n:
            print(n,"is a perfect no")
    else:
        print(n,"is not a perfect no")
