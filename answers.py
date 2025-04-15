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


    
for animal in [dog1,dog2, cat1]:
   animal.speak()



cat1 = Cats(4)
print(cat1.legs)


#answer2

#Create a program that includes animals or vehicles with the same action (like move()). 
#However, make each class define move() differently (for example, Car.move() 
# prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️)

class Human:
    def speak(self):
        print("Animal is speaking")

class Kenyan(Human):
    def speak(self):
        print("Jambo!")

class English(Human):
    def speak(self):
        print("Hello!")

class Congolese(Human):
    def speak(self):
        print("Mbote!")

Humanity = [Kenyan(), English(), Congolese()]

for Human in Humanity:
    Human.speak()
    


