class A:
    def __new__(cls):
        ob = super().__new__(cls)
        print("inside new constructor")
        return "abc"

    def __init__(self):
        print("inside init constructor")
ob = A()
