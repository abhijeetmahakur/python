class C:
    name = "Abhijeet"
    mark = 70

    def get_data(self, a, r):
        self.a = a
        self.r = r

    def show(self):
        print("a:", self.a)
        print("r:", self.r)


ob = C()
ob.get_data(2, 56)
ob.show()
