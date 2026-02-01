n=int(input("Enter a no:"))
i=1
c=0
print("factors ofn","are")
while (i<=n):
    if n%i==0:
        c=c+1
        i=i+1
        if c==2:
            print("prime no")
        else:
            print("not prime no")



 #when i is smaller than n
n=int(input("Enter a no:"))
i=2
c=2
print("factors of n","are")
while (i<n):
    if n%i==0:
        c=c+1
        break
        i=i+1
        if c==0:
            print("prime no")
        else:
            print("not prime no")


