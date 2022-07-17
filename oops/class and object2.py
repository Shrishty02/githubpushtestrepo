
class Person:

    def __init__(sudh,name,surname,emailid,year_of_birth): #self is a pointer to a class and next are variable
        sudh.name=name #sudh.name is calss variavle and name is allocation
        sudh.surname = surname
        sudh.emailid = emailid
        sudh.year_of_birth= year_of_birth

    def age(sudh, current_year):
        return current_year-sudh.year_of_birth

anuj_var =Person("anuj","bhandhari","anuj@gmail.com",1994) #anuj is class variable whic is caled OBJECT
sudh =Person("sudhanshu","kumar","sudh@gmail.com",12345) 
gargi=Person("gargi","kar","gar@gmail.com",2002)   #anuj is variable of person class
print(sudh.age(2022))
print(anuj_var.age(2022))
s ="siudh"
s.upper()
