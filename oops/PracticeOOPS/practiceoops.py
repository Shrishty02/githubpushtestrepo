class computer:
    def __init__(self):
        self.name ="Navin"
        self.age= 29

    def update(self):
        self.age =30

    def compare(self,others):  # c1 becomes self
        if self.age == others.age:
            return True
        else :
            return False

c1= computer()
c2= computer()
c2.update()
print(c1.compare(c2))


