import logging
from typing import final
logging.basicConfig(filename="task1.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')


class question1:
    
    def reverse_a_list(self,list1):
        self.list1=list
        
        try :
            logging.info('resource open')
            logging.info(list1[::-1])
        except Exception as e:
            logging.exception(e)

        finally:
            logging.INFO("resource closed")

    def accese_no_out_of_list(self, list1):
        
        for i in list1:
            if i==234 :
                i.remove()
                logging.INFO(list1)
    
    def access_a_num(self,list1):
        for num in list1:
            want_num= list1.index(num)
            logging.INFO(num)

    def try_to_extract_list(self,list1):
        for list in list1:
            for items in list:
                logging.INFO(items)

    def extract_sudh(self,list1):
        a="sudh"
        try:
            logging.INFO(list1.index(a))
        except Exception as e:
            logging.exception(e)
    

task= question1()
task.reverse_a_list = ( [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])
logging.info(task.list1)           



    





