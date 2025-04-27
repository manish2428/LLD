from abc import ABC,abstractmethod

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes sound")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says MEOWWWWW!!!!")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says BHOWWWWW!!!!")
    
cat = Cat("Jimmy")
cat.speak()

dog = Dog("Bhote")
dog.speak()

    
'''
Inheritance allows one class (child) to reuse and extend the behavior of another class (parent)

- Reuse common code
- Maintain a hierarchy (DRY principle)

'''