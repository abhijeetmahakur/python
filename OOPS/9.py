class A:
    obj=None
    def __new__(cls,val):
        if cls.obj==None:
            cls.obj=super().__new__(cls)
        return cls.obj
    def ___init__(self,val):
        self.val=val