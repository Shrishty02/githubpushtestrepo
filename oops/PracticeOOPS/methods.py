class student:
    school ="shrishty"
    def __init__(self,m1,m2,m3):
        self.m1 =m1
        self.m2 =m2
        self.m3 =m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    @classmethod
    def getschool(cls):
        return cls.school
    
    @staticmethod
    def Findanything(a,b):
        return a+b


    #def set_m1(self,new_values):
        #return self.m1 = new_values

s1 = student(34,67,32)
s2= student(23,45,67)
print(s1.avg())
print(student.getschool())
print(student.Findanything(23,89))