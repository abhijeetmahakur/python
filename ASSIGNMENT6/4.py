class Car:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @make.setter
    def make(self, make):
        self.__make = make

    @model.setter
    def model(self, model):
        self.__model = model


c1 = Car('Abhijeet', 'bmw')
c2 = Car('teja', 'audi')

print(c1.make)
print(c2.model)
