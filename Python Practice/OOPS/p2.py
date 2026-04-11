class Vehicle:
    def __init__(self, brand, color, yom):
        self.brand = brand
        self.color = color
        self.YOM = yom

    def stating(self):
        print("Starting car!!", self.brand)

    def stopping(self):
        print("Stopping!!")


BMW = Vehicle("BMW", "RED", 2000)
BMW.stating()
Maidish = Vehicle("MSD", "RED", 2005)
Maidish.stating()
