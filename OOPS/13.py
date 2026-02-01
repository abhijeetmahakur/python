class ABC:
    cname="Iter SOA University"
    @classmethod
    def show(cls,data):
        name,mark=data.split("-")
        print(cls.cname)
        return cls(name,int(mark))
    
def __init__(self,name,mark):
    self.name=name
    self.mark=mark
ob=ABC("abcd",89)
ob1=ABC("xyz",450)
print(ob.name,ob.mark)
print(ob.__dict__)
print(ob1.__dict__)