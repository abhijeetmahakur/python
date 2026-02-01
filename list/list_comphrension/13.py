n=int(input("Enter a number:"))
prime=[i for i in range (2,n)if n%i==0]
if len(prime)==0:
    print("prime")
else:
    print("not prime")