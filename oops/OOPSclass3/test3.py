class ineuron:
    def student(self):
        print("print the detail of all the students")
    def achivers(self):
        print("print the list of all the achievers")
    def hall_of_fame(self):
        print("print everyone")

class ineuron_vision(ineuron):
      
    def student(self):   
        print("these are the students filtered for this list")

a= ineuron_vision()
a.student()

#When the parent and child class has the same method the method in the child class overwrites the parent class(Method overriding)

