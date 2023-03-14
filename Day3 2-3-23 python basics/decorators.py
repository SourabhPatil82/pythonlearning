#when you need to change the behavior of a function without modifying the function itself.

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks")
    return mfx

@greet
def hello():
    print("hellow world")

#@greet
# def add(a,b):
#     print(a+b)


#or greet(hello)()
hello()