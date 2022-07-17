#incaptulation you are not supoose to allow the useer to modify the data directly but it can be done by class method
class ineuron:
    def __init__(self): 
        self.students1="data science"

    def students(self):
        print(self.students1)
i= ineuron()
i.students()
i.students1 ="data analytics"
i.students()

class ineuron1:
    def __init__(self): 
        self.__students1="data science"

    def students(self):
        print(self.__students1)

    def student_change(self,new_value):
        self.__students1 = new_value
i1= ineuron1()
i1.students()
i1.__students1 ='big data'
i1.students()
i1.student_change("sudh")
i1.students()