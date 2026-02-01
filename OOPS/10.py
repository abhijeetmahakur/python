class Abc:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f"name = {self.name}\nroll = {self.roll}"

ob = Abc("Abhijeet", 101)

print(ob)
print(ob.__str__())


