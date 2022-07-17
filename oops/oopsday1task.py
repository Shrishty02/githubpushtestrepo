import logging
logging.basicConfig(filename= "stringTask.log", level =logging.DEBUG)

class StringTask:
    def extract_data(self,s):
        try:
            logging.info("The given string of this operation is %s :", s)
            s1=s[1:300:3]
            logging.info("the output ogf the operation is %s",s1)
            return s1
        except Exception as e:
            logging.exception("The exception we have got is :" + "\n" + str(e))

    def reverse_the_string(self,s):

        try:
            logging.info("the given string for this operation is %s :",s)
            s2=s[::-1]
            logging.info("the output after operation is %s:", s2)
            return s2
        except Exception as e:
            logging.exception("the exception is " + "\n" + str(e))
        
    def split_uppercase_string(self,s):
        try:
            logging.info("the given string is %s", s)
            s3=s.upper().split(' ')
            logging.info("the output of the operation is %s", s3)
            return s3
        except Exception as e :
            logging.exception("the exception we have got is " + "\n" + str(e))
    
    def conversion_to_lower_string(self, s):
        try:
            logging.info("the given string is %s", s)
            s5=s.lower()
            logging.info("the output of the string is %s:", s5)
            return s5
        except Exception as e:
            logging.exception("the exception is :" +"\n" + str(e))
    
    def conversion_to_capitalize_string(self, s):
        try:
            logging.info("the given string is %s", s)
            s7=s.capitalize()
            logging.info("the output of the coversion is %s",s7)
            return s7

        except Exception as e:
            logging.exception("the exception is " + "\n" + str(e))
  
lower_string= StringTask()
logging.info(lower_string.conversion_to_lower_string("this is My First Python programming class and i am learNING python string and its function"))