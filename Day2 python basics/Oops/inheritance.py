class employee:
    def __init__(self,name1,email1) :

        self.name=name1
        self.email=email1
       

    def show(self):
        print(f"hii my name is {self.name}and my email is {self.email}")

    
class Developer(employee):
    def showLang(self):
        print("java")




a=employee("sourabh","sourabh@gmail.com")


b=Developer("sourabh2","sourabh@gmail.com")

a.show() 
b.show()
b.showLang()