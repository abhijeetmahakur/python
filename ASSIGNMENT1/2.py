op=input("Enter the operation<add,sub,mul,div,mod>")
a=(inpuit("Enter the first number:"))
b=(inpuit("Enter the second number:"))
op=op.lower()[0:3]
if op=="add":
    c=a+b
    print("result:",c)
elif op=="sub":
    c=a-b
    print("result:",c)
elif op=="div":
    if b==0:
        print("error division by zero")
    else:
        c=a/b
    print("result:",c)
elif op=="mul":
    c=a*b
    print("result:",c)
elif op=="mod":
    c=a%b
    print("result:",c)
else:
    print("Invalid Operation")


