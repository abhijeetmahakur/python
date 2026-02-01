a=int(input("enter the first no"))
b=int(input("enter the second no"))
s=a+b
d=a-b
m=a*b
d=a/b
mod=a%b
pow=a^b
df=a//b
print("sum",s)
print("differece",d)
print("multipliction",m)
print("division",d)
print("modulus",mod)
print("power",pow)
print("floor division",df)







#OF IF ELSE
a=int(input("enter the first no:"))
b=int(input("enter the second no:"))
m=int(input("Enter the choice:"))
op=input("Enter the operator:")
if m==1 or op=="+":
    print(a+b)
elif m==2 or op=="-":
   print(a-b)
elif m==3 or op=="*":
   print(a*b)
elif m==4 or op=="/":
   print(a/b)
elif m==5 or op=="%":
   print(a%b)
elif m==6 or op=="//":
   print(a//b)
elif m==7 or op=="**":
   print(a**b)
else:
   print("INVALID RESPONSE")

    