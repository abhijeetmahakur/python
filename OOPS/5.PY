class Rectangle_operation:
    op1 = "Rectangular operation"

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def peri(self):
        return 2 * (self.l + self.b)

    def display(self):
        area = self.area()
        peri = self.peri()
        print("Area of the rectangle:", area)
        print("Perimeter of the rectangle:", peri)


r1 = Rectangle_operation(3, 4)
r1.display()
