def chkpall(st):
    for i in range(0,len(st)//2):
        if st[i]!=st[len(st)-i-1]:
            return False
    return True
def chkpall1(st):
    st=st.translate(str.maketrans("","",str.puchtuation))
    left=0
    right=len(st)-1
    while left<right:
        if st[left]!=st[right]:
            return False
        left+=1
        right-=1
    return True
st=input("Enter the String:")
if chkpall(st):
    print("Palindrome")
else:
    print("not palindrome")
    
if chkpall1(st):
    print("Palindrome")
else:
    print("not palindrome")