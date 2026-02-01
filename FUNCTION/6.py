str1=str(input("enter a string:"))
if(len(str1)%2==0):
    mid=(len(str1)//2)+1
else:
    mid=(len(str1)//2)
    result=str1[mid-1:mid+1]
    print(result)