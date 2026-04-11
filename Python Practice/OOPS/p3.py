class STUDENT:
    def gettingDetail(self, name, marks):
        self.name = name
        self.marks = marks

    def displayingDetail(self):
        print("Displaying detail")
        print(f"{self.name} with {self.marks} marks.")


stud1 = STUDENT()
stud1.gettingDetail("Himanshu", 80.9)
stud1.displayingDetail()
stud1.gettingDetail("Manish", 99.9)
stud1.displayingDetail()
stud1.gettingDetail("Abhinandan", 89.9)
stud1.displayingDetail()
