# Write a method inside the Laptop class called specs() that prints the brand and model.

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    
    def stop(self):
        print(f"The car {self.model} {self.color} has stopped!")

car1 = Car("ABC", "asd")
car1.stop()

