
class Person:

    def __init__(self,name,surname,emailid,year_of_birth): #self is a pointer to a class and next are variable
        self.name=name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth= year_of_birth

anuj_var =Person("anuj","bhandhari","anuj@gmail.com",1994) #anuj is class variable whic is caled OBJECT
sudh =Person("sudhanshu","kumar","sudh@gmail.com",12345) 
gargi=Person("gargi","kar","gar@gmail.com",2002)   #anuj is variable of person class
print(anuj_var.name)
print(anuj_var.surname)
print(anuj_var.emailid)
print(sudh.name)
print(gargi.year_of_birth)
print(type(sudh))
