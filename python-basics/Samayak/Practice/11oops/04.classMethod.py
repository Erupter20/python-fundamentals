# 4. Create a class called Vehicle and add a method called start_engine() that prints "Engine started."

class Vehicle:
    def __init__(self,model, brand ):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.model} {self.brand}'s Engine Started.")

vehicle = Vehicle("HM" , "Contessa")
vehicle.start_engine()