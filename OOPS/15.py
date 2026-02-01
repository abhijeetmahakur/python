class ABC(int):
    def __new__(cls,val):
        ob=super().__new__(cls,val)
        return ob
    def __init__(self,val):
        self.val=(val)
x=Myint(5)
print(id(x))
x=x+1
print(id(x))
print(type(x))        