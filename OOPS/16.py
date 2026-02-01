class A:
    def __init__(self):
        print("inside A")
        return B()
class B:
    def __init__(self):
        print("inside b")
ob=B()
ob=A()
        