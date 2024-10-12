class Bob:
    def speak(self, sound):
        print(f"This animal says... {sound}~")

class Jane(Bob):
    def bark(self):
        self.speak("Wan wan")

class Laura(Bob):
    def meow(self):
        self.speak("Nya nya")


jane = Jane()
jane.bark()

laura = Laura()
laura.meow()
print("\nNew example here:\n")

# new type of structure
class Bob:
    def speak(self):
        print(f"This animal says... {self.sound}~")

class Jane(Bob):
    sound = "wof wof"

class Laura(Bob):
    sound = "nya nya"

#print print
animals = [Jane(), Laura()]
for animal in animals:
    animal.speak()


# new type of structure
class Bob:
    def __init__(self, res=10):
        self.res = res

    def calc(self):
        self.res = self.x + self.y
        print(self.res)

    def print_res(self):
        print(self.res)

class Jane(Bob):
    x = 10
    y = 90

class Laura(Bob):
    x = 8
    y = 39

maths = [Jane(), Laura()]
for math in maths:
    math.calc()

# print print
maths[0].print_res()

bob = Bob()
bob.print_res()

