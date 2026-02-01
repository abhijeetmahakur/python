class A:
    def __init__(self,val):
        self.val=val
        print(self.val)
ob=A(20)
print(id(ob))
ob1=A(45)
ob=A(10)
