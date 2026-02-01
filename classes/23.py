n=int(input("Enter a no:"))
i=1
c=0
print("factors ofn","are")
while (i<n):
    if n%i==0:
        c=c+1
        i=i+1
print("no of factors of",n,"is",c)