class Person:
    def __init__(self,gender):
        self.gender=gender
class College:
    def __init__(self):
        self.p1=Person("Male")
        self.p2=Person("Female")
c=College()
print(c.p1.gender)
print(c.p2.gender)

