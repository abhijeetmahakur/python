class A:
    def get_data(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def show(self):
        print("First number:",self.num1)
        print("Second number:",self.num2)
ob=A()
ob.get_data()
ob.show_data()
