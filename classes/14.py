n=int(input("Enter a no:"))
sum=0
while(n>0):
    digit=n%10
    sum=sum+digit
    n=n//10
    print("sum os digit is",sum)
