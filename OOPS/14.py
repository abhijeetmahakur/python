class Temp1:
    @staticmethod
    def c_to_f(c):
        return c*9/5+32
    @staticmethod
    def f_to_c(f):
        return (f-32)*5/9
ob=Temp1()
print(ob.f_to_c(100))
print(ob.c_to_f(37.78))
    
    