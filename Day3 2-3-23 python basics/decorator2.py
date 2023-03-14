def decor(fun):
    def inner():
        a=fun()
        add=5+a
        return add
    return inner



def num():
    return 10





res=decor(num)
print(res())