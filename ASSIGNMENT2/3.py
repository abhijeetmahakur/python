stack=[]
def isempty():
    if len(stack)==0:
        return True
    else:
        return False
def push(item):
    stack.append(item)
def poped():
    if isempty():
        print("Stack Underflow")
        return -1
    else:
        return stack.pop()
def disp(item):
    for i in stack[-1::-1]:
        print(i,end=" ")

def rpn(exp):
    for i in exp:
        if i.isdigit():
            push(i)
        else:
            op1=poped()
            op2=poped()
            if i=="+":
                push(int(op2)+int(op1))
            elif i=="-":
                push(int(op2)-int(op1))
            elif i=="*":
                push(int(op2)*int(op1))
            else:
                print("invalid operator")
print("-----------Stack Operation-----------")
while 1:
    print("press 1 for push")
    print("press 2 for pop")
    print("press 3 for disp")
    print("press 4 for rpn")
    print("press 5 for exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        item=int(input("Enter the item to push"))
        push(item)
    elif ch==2:
        k=popped()
        if k==-1:
            print("stack underflow")
        else:
            print("popped element is:",k)
    elif ch==3:
        disp()
    elif ch==4:
        exp=input("Enter the postfix")
    elif ch==5:
        break
    
    