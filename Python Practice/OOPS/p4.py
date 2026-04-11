class CAR:
    def settingDetail(self, brand, price):
        self.brand = brand
        self.price = price

    def displayDetail(self):
        print(f"Car Name {self.brand} and price {self.price}")


obj = CAR()
obj.settingDetail("BMW", 1203040)
obj.displayDetail()
