class Math:
    @staticmethod
    def add(a,b):#not associated with any class instance
        return a+b
    

print(Math.add(2,3))

a=Math()
print(a.add(2,1))
