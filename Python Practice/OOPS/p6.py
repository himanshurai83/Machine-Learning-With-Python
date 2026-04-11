class STUD:
    count = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        STUD.count += 1

    def __str__(self):
        return f"Name: {self.name} and Marks: {self.marks}"


s1 = STUD("Himanshu", 65)
s2 = STUD("Himanshu", 65)
print(s1)
print(f"Total objects : {STUD.count}")
