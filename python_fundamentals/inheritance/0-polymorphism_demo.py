#!/usr/bin/env python3

class Animal:
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"
    
class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())
