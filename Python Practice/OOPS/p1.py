class Animal:
    def sound(self):
        print("Animal sounds!!")


class DOG(Animal):
    def sound(self):
        print("DOGs Barks!!")


dog = DOG()
dog.sound()
