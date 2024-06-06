import os
import sys

def get_error_message(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in the python script [{0}]; Line no. [{1}] \n Error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    return error_message

class HelmetException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__()
        self.error_message = get_error_message(
            error=error_message, error_detail=error_detail
        )
        
    def __str__(self):
        return self.error_message