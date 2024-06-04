from src.exceptions import CustomException
from src.logger import logging
import sys

if __name__== "__main__":
    logging.info("logging started")
    try:
        a=1/0
    except Exception as e:
        logging.error("Sample error raised")
        raise CustomException(e,sys)