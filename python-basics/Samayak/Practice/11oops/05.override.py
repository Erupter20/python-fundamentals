# 4. Create a class called Vehicle and add a method called start_engine() that prints "Engine started."

class Vehicle:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model} engine started")

car1 = Vehicle("HM" ,"Contessa")
car1.start_engine()