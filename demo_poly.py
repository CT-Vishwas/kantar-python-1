# Many forms
# Functions are first class citizens ( I can pass the functions)

class Parrot:
    def speak(self):
        return "Squawk"
    
class Dog:
    def speak(self):
        return "bark"
    
def animal_sound(animal):
    print(animal.speak())

c = Dog()
p = Parrot()

animal_sound(c)
animal_sound(p)