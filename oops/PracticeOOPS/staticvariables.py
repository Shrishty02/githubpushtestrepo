class Car:
    def __init__(self): #instance variable
        self.mil=10
        self.com ="BMW"

    wheels = 4 #class variable

c1 =Car()
c2=Car()
c1.mil =5

Car.wheels =5 #if we change the class variable it will change the whole thing that has been changed.


print(c1.mil , c1.wheels)
print(c2.mil, c2.wheels)