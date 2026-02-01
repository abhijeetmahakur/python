
class Student:
    @property
    def roll(self):
        return self.__roll
    @property
    def marks(self):
        return self.__marks
    @property
    def age(self):
        return self.__age
    @roll.setter
    def roll(self,roll):
        self.__roll=roll
    @marks.setter
    def marks(self,marks):
      self.__marks=marks
    @age.setter
    def age(self,age):
       self.__age=age
ob=Student()
ob.roll=24
ob.marks=124
ob.age=18
print(ob.roll)
       