import sys
from src.logger import logging


def error_messsage_detail(error, error_details:sys):
    _, _, exc_details = error_details.exc_info()
    filename = exc_details.tb_frame.f_code.co_filename
    lineno = exc_details.tb_lineno
    error_message = f"Error occurred at script {filename} line {lineno}\
        message {error}"
    
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_details:sys):
        super().__init__(error)
        self.error_message = error_messsage_detail(error,error_details)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        logging.info("exception.py created successfully")
    except Exception as e:
        logging.info(e)
        raise CustomException(e, sys)