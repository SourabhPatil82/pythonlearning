class Dog :
    
    def __init__(self,name,age) -> None:
        self.name=name
        self.me="ss"
        self.age=age
    
        #print(name)
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

   
    def set_name(self,name1):
        self.name=name1
        
    def bark(self):
        print("in function")
        print("bark bark bark")
    def sum(self,a,b):
        return a+b

d=Dog("tom")
print(d.name)
print(d.me)
d.set_name("changed name")
print(d.get_name())
e=Dog("jerry")
print(e.get_name())
#d.bark()
#print(d.sum(4,5))


     
