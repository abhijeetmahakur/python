a=b=25
print("value of a is:",a)
print("value of a is:",b)



#memory location are different
a,b,c=25,30,39
print("value ofa is:",a)
print("value ofa is:",b)
print("value ofa is:",c)
print("address of a is:",id(a))
print("address of b is:",id(b))
print("address of c is:",id(c))


#memory location are different
a,b,c=25,30,"abhi"
print("value ofa is:",a)
print("value ofa is:",b)
print("value ofa is:",c)
print("address of a is:",id(a))
print("address of b is:",id(b))
print("address of c is:",id(c))



#swap of two number without using arithmatic operator
a=5
b=10
a=a^b
b=a^b
a=a^b
print(a)
print(b)