class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def __str__(self):
        return f"{self.name}({self.species})"
ob=Animal("jucicy","cat")
print(ob.__str__())