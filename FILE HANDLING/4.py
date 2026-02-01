with open("nums.txt","r")as f:
    data=f.read()
list=data.split(",")
for i in list:
    n=int(i)
    if n%2==0:
        print(n)