def add(*args):
    sum=0
    print(type(args))
    for arg in args:
        sum+=arg
    return sum

def calculate(n, **kwargs):
    print(type(kwargs))
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)
class Car:
    def __init__(self, **kw):
        self.make=kw.get("make")
        self.model=kw.get("model")



print(add(1,2,3,4,5,6))
calculate(2,add= 3, multiply=4)
car= Car(make="Seat", model="Leon")
print(car.make)
print(car.model)