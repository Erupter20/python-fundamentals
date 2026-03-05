# 7. Create a base class called Animal with a method called speak() and a subclass Dog that overrides the speak() method.

# Parent class
class Animal:
    def speak(self):
        print("Generic animal sound")

#Child class
class Dog:
    def speak(self):
        print("woof!") # Overridden

dog= Dog()
dog.speak()