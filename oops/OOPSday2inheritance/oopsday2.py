from utils.util1 import person2     
#package means folder?dicrectorty module means fike

obj=person2("sudhanshu","kumar",1234567)
print(obj.yob1)






class person1:
    def __init__(self,name, surname, yob):
        self._name=name             #_name underscore phle then its protected
        self.__surname=surname        #__ doble private one
        self.yob1 =yob
sudh=person1("sudhanshu","kumar",1990)
print(sudh._name)
print(sudh._person1__surname)    #to acccess a private use class name _classname eg _person
