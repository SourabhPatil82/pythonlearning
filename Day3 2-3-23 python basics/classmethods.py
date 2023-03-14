class Employee:
    company="HPE"

    def show(self):
      print(f"The name is {self.name} and company is{self.company}")

    @classmethod
    def changeCompany(class1,newName):
       class1.company=newName


e1= Employee()
e1.name="sourabh"
e1.show()
e1.changeCompany("google")
e1.show()
print(Employee.company)