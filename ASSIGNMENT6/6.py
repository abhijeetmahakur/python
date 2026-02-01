class A:
    def __new__(cls):
        print("Inside __new__ method")
        return super().__new__(cls)

    def __init__(self):
        print("Inside __init__ method")


ob = A()
