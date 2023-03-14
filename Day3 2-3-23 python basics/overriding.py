class shape:
    def area(self):
        print("In parent")
class shape1:
    def area1(self):
        print("in parent 2") 



class circle(shape,shape1):#multiple inheritance
    def __init__(self) -> None:
        super().__init__()
    def area(self):
        print("in child")


s1=shape()
s1.area()

c1=circle()
c1.area()
c1.area1()