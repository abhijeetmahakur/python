n=int(input("Enter a no:"))
k=n
rev=0
while(n>0):
    dig=n%10
    n=n//10
    print(rev)
    if rev==k: 
     print(k,"is a pallindrome no")
    else:
       print(k,"is not pallindrome no")