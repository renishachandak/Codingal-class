class Parrot:

    def __init__(self, name , age , color):
        self.name = name
        self.age = age
        self.color = color


    def sing(self, song):
        return "{} sings {}".format(self.name, song)    

    def dance(self):
        return "{} is now dancing".format(self.name)

    def fly(self):
        return "{} is now Flying".format(self.name)

    def describe(self):
        return "{} is {} in color".format(self.name, self.color)

hii = Parrot("Hii", 22, "blue")
moti = Parrot("Moti", 5, "green")

print(hii.sing("Happily"))
print(hii.dance())

print(moti.fly())
print(moti.describe())