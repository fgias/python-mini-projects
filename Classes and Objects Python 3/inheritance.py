class Shark:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return self.name + " is swimming."

    def be_awesome(self):
        return self.name + " is being awesome."


class BabyShark(Shark):
    def cry(self):
        return self.name + " is crying because it is a baby."

jo = Shark("Jo")
sammy = BabyShark("Sammy")

print(jo.swim())
print(sammy.swim())

print(jo.be_awesome())
print(sammy.be_awesome())

print(sammy.cry())


