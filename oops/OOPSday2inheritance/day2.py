import oopsday2
print(oopsday2)
obj3=oopsday2.person1("sudhanshu" ,"kumar" ,1994)
print(obj3.yob1)
print(obj3._name)
print(obj3._person1__surname)


class person:
    _name ="sudh"
    __surname ="kumar"
    yob =1990

    def _age(self,current_year):
        return current_year-self.yob
    def __age1(self,current_year):
        return current_year-self.yob

obj =person()
print(obj._age(2022))
print(obj._person__age1(2022))

class employee(person): #inheritance person is parent class and employ is child
    _name ="sudhnashu"
    __surname="singh"
    yob=1991

obj1=employee()
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._employee__surname)
print(obj1._age(2022))
print(obj1._person__age1(2022))