class person:
    def __init__(self,name1,email1) :

        self.name=name1
        self.email=email1

    def info(self):
        print(f"hii my name is {self.name}and my email is {self.email}")

    
a=person("sourabh","sourabh@gmail.com")
b=person("sourabh2","sourabh@gmail.com")

a.info() 
b.info()