import sys
from src.logger import logging

def error_msg_details(error, error_details:sys):
    _,_,exc_info = error_details.exc_info()
    file_name = exc_info.tb_frame.f_code.co_filename
    error_msg="Error in script [{0}] line [{1}] message - [{2}]".format(
        file_name, exc_info.tb_lineno,str(error)
    )
    return error_msg

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys ):
        super().__init__(error_message)
        self.error_message=error_msg_details(error_message, error_details=error_details)
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message