import math
print("I am sourabh")
a=3
print(a)
print(type(a))
list=[1,"ss",'d']#muttable
print(list)
touple=(1,2,3)
print(touple)#immutable
print ( math.gcd(3,6))
'''hgjfgsjfhsgfjshgjfhsdgfjuds'''
name="  soirabh       "
print(name[1])
print(name[2:5])

print(name.strip()) #to remove spaces
print(len(name))#to measure length
print(name.replace("s","p"))

dict1={"key1":"value1","key2":"value2","key3":10}

print(dict1)




a="pri"
b="swant"

c="I am {1} {0} from kop".format(a,b)
print(c)

d=f"i am {a} {b}from kop"
print(d)

lst=[1,3,45,6,7,8,1]
lst.append(100)
print(lst)
lst.insert(1,900)
del  lst[1]
print(lst)


set={1,1,22,22,34,44,44,4,44,44,44}
set.add(12)
set.update([1,22,22,4,5,6,77,8,9])
print(set)



age=18
if(age>18):
    print("U can drive")
elif(age==18):
    print("u r 18")
else:
    print("U can not drive")

    '''list
    
    tuple 
    
    set 
    
    dicstionary
    
    
    
    for while break continue'''

def fun():
    print("im iin function")

fun()

def sum(a,b):
    return(a+b)

print(sum(17,7))


class Employee:
    def __init__(self,gname,gsalary):
        self.name=gname
        self.salary=gsalary

sourabh=Employee("abhi",100000)
print(sourabh.name)
print(sourabh.salary)
        