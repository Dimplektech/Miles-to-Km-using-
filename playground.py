def add(*nums):
    total = 0
    for i in nums:
        total = total + i

    return  total

print(add(5,7,8,2))



def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(3,add=3, multiply=5)


### creating  class using optonal arguments
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") # if we use .get instead of kw["make"],
        # we dont get error if dont pass arguments and output will be None.
        self.model = kw.get("model")

my_car = Car(make = "Nissan")
print(my_car.model) # output will be None



