def decor1(fun):
    def inner():
        print("before enhancing function")
        fun()
        print("after enhancing function")
    return inner
    
@decor1
def num():
    print("use this fun for trail")



num()