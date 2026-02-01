class Abc:
    name ="Abhijeet Mahakur"
    score=20000
    def __init__(self,nm,ag):
        #print(self)
        self.name=nm
        self.age=ag
    def show(self):
        print("name:",self.name)
        print("age:",self.age)
ob=Abc()
print(ob)
print(Abc.name)
print(Abc.score)
