class person2:
    def __init__(self,name, surname, yob):
        self._name=name             #_name underscore phle then its protected
        self.__surname1=surname        #__ doble private one
        self.yob1 =yob
sudh=person2("sudhanshu","kumar",1990)
print(sudh._name)
print(sudh._person2__surname1)    #to acccess a private use class name _classname eg _person
