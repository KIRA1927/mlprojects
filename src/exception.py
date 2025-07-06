import sys
from src.logger import logging
#sys is a built-in module that provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.
def error_message_detail(error, error_detail: sys):
    """
    This function takes an error and its details, and returns a formatted string with the error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script: [{0}] at line number: [{1}] with message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error) )
    return error_message

class CustomException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    It overrides the constructor to provide a detailed error message.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.info("An error occurred, raising CustomException.")
#         raise CustomException(e,sys)
        
    # This will raise a CustomException with the error message formatted by error_message_detail function.