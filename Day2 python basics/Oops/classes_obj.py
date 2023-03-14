class person:
    name="sourabh"
    email="sou@hmail.com"
    city="pune"

    def info(self):
        print(f"my name is {self.name} i am from {self.city}")


a=person()
b=person()
c=person()

b.name="ram"
b.info()

a.name="shubham"
a.info()