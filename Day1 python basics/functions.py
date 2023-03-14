def calculator(a,b):
    return a+b

print(calculator(1,2))


def isGreater(a=1,b=1,c=1):# u may or maynot provide the value at ti,e of function is calling
    if(a>b):
        return "a is greater than b"
    elif(a>c):
        return "a is greater than c"
    else:
        return "a is smaller"
print(isGreater(10,1,1))

"""
types of args in function:
default arg

keyword arg

variable length arg
 
req arg
"""

def average(*numberss):# taken ip as a touple()
    sum=0
    for i in numberss:
        sum=sum+i
    print("Average is : ",sum/len(numberss))

average(2,3,4,1)