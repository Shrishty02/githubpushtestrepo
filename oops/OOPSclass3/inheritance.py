class car:
    def __init__(self, body, engin,tyre):
        self.body=body
        self.engin=engin
        self.tyre=tyre

    def milage(self):
        print("milage of this car ")
c=car("sold","v6","radoial")
print(c)

class tata(car): #car is parent class so we have to pass the value like parent class

    pass

t=tata("solid1","v8","radial1")
print(t)
print(t.milage())
