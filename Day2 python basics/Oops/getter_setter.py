class myclass:
    def __init__(self,value) -> None:
        self.value=value

    def show(self):
        print(f"Value is {self.value}")


    @property
    def tenTimesValue(self):
        return 10*self.value
    
    @tenTimesValue.setter
    def tenTimesValue(self,new_value):
        self.value=new_value/10


obj=myclass(10)
obj.tenTimesValue=67
obj.show()