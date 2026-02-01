class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.__marks = 0
        self.grade = ""

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            self.calc_grade()
        else:
            print("Invalid marks!")

    def get_marks(self):
        return self.__marks

    def calc_grade(self):
        if self.__marks >= 90:
            self.grade = "A"
        elif self.__marks >= 80:
            self.grade = "B"
        elif self.__marks >= 70:
            self.grade = "C"
        elif self.__marks >= 60:
            self.grade = "D"
        elif self.__marks >= 50:
            self.grade = "E"
        else:
            self.grade = "F"

    def show_details(self):
        print(f"Name: {self.name}, Roll: {self.roll_no}, Marks: {self.__marks}, Grade: {self.grade}")


s1 = Student("Abhijeet", 101)
s1.set_marks(92)

s2 = Student("Teja", 102)
s2.set_marks(75)

s1.show_details()
s2.show_details()
