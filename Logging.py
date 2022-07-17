import logging
logging.basicConfig(filename="loggingtest2.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info("this is my log with time stamp")
