class EMP:
    def setDetail(self, name, salary):
        self.name = name
        self.salary = salary

    def incrementSalary(self):
        print("Increasing Salary by 10%")
        self.salary += self.salary*.1

    def displayDetail(self):
        print(f"EMP name: {self.name} Salary {self.salary}")


emp = EMP()
emp.setDetail("Himanshu", 10000)
emp.displayDetail()
