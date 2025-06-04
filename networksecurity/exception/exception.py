import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message,exc_tb):
        self.error_message = error_message
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name,self.lineno,str(self.error_message))
if __name__ == "__main__":
            try:
                logger.logging.info("Enter the try block")
                a = 1/0
                print("This will not be printed",a)
            except Exception as e:
                _, _, exc_tb = sys.exc_info()
                raise NetworkSecurityException(e, exc_tb)

