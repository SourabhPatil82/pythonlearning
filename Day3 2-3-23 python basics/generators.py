#generators are spl type of functions that allow you to create an iterable seq of values
#to generate values on the fly instead of stored once in memory
#to save memory
#to work with large data set

def my_generator():
    for i in range(5):
        yield i

gen=my_generator()

#the next funct is used to request next value from the generator
print(next(gen))
print(next(gen))
print(next(gen))

# for j in gen :
#     print(j)