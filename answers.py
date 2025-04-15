# Answer 1

class Animals:
    def __init__(self,legs):
        self.legs = legs


class Cats(Animals):
    pass

class Dogs(Animals):
    pass


class Cat:
    def __init__(self, color, race):
        self.color = color
        self.race = race

    def speak(self):
        print("Meow! Meow!")

    
cat1 = Cat("black","Egyptian Mau")
cat2 = Cat("brown-black","Somali")
cat3 = Cat("green-black","Serengeti cat")

print(cat1.color)
print(cat1.race)

class Dog:
    def __init__(self,color,race, name):
        self.color = color
        self.race = race
        self.name = name
    
    def speak(self):
        print("Woof! Woof!")

dog1 = Dog("dark-brown", "Doberman", "Indus")
dog2 = Dog("brown", "African Dog", "Chui")

print(dog1.name)
print(dog1.race)
print(dog2.name)
print(dog2.race)


    
for animal in [dog1, cat1]:
   animal.speak()



cat1 = Cats(4)
print(cat1.legs)


