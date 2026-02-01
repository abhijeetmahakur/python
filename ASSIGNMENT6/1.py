class Student:
    def __init___(self,name,roll):
        self.name=name
        self.roll=roll
    def show(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
n=int(input("Enter no of students you want to add"))
stud=[]
for i in range(n):
    print(f"Students-{i+1}'s information")
    name=input("Enter the name")
    roll=int(input("Enter the rollno:"))
    ob=Student(name,roll)
    stud.append(ob)
print("Student Information")
for i in stud:
    i.show()