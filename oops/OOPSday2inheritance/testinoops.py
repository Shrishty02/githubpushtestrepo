from utils.util1 import person2     
#package means folder?dicrectorty module means fike
import logging
logging.basicConfig(filename ="conceptcheck.log", level = logging.DEBUG)

obj=person2("sudhanshu","kumar",1234567)
logging.info(obj.yob1)






class person1:
    def __init__(self,name, surname, yob):
        self._name=name             #_name underscore phle then its protected
        self.__surname=surname        #__ doble private one
        self.yob1 =yob
sudh=person1("sudhanshu","kumar",1990)
logging.info(sudh._name)
logging.info(sudh._person1__surname)    #to acccess a private use class name _classname eg _person
