class A:
    def __init__(self,v1,v2,v3):
        self.v1=v1
        self.v2=v2
        self.v3=v3
    def show(self):
        print("Public:v1",self.v1)
        print("Private:v1",self.v2)
        print("Protected:v1",self.v3)
ob1=A(3,4,6)
ob1.show()
ob1.__v1=10
ob1_v2=300
ob1.v3=8779
ob1.show()
print(ob1.__dict__)
