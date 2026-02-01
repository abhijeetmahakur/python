n=int(input("Enter a no:"))
k=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if k==rev:
    print(k,"is an reverse no",rev)
else:
    print(k,"is not an reverse no",rev)

