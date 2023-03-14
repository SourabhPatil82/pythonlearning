x=10

def my_function():
    y=5
    global x #to change global scope vaiable
    x=x+100
    print(y)

my_function()
print("value of global x got changed in func",x)