class  parentClass:
    def parent_method(self):
        print("Inside parent ")

class childClass(parentClass):
    def childMethod(self):
        print("inside child ")
        super().parent_method()


childOject=childClass()
childOject.childMethod()


class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id


    def __str__(self) -> str:
      return f"The name of employee is {self.name}"

    
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang

p1=Programmer("sourabh",521,"python")
e1=Employee("amit",100)
print(p1.name)
print(p1.id)
print(p1.lang)
print(e1)