l=[1,22,3,4,5,6,7,2]

def cube(a):
    return a*a*a

def filter_func(a):
    return a>4

list1=list(filter(filter_func,l))

print(list1)

for items in list1:
    print(items)



newlist=list(map(cube,l))

print(newlist)