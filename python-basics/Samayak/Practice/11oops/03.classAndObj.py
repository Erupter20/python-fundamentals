# Create an object of the Laptop class with brand "Dell" and model "Inspiron 15".

class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
laptop1 = Laptop("Dell", "Inspiron 15")

print(laptop1.brand)