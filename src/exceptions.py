import sys
from src.logger import logging

def error_details(error):
    _, _, exe_tb = sys.exc_info()
    error_message = (
        f"Error occurred in script "
        f"[{exe_tb.tb_frame.f_code.co_filename}] "
        f"at line [{exe_tb.tb_lineno}] "
        f"error message [{error}]"
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error):
        super().__init__(error)
        self.error_message = error_details(error)

    def __str__(self):
        return self.error_message


