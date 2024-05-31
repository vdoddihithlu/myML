import logging
import os   
import sys
from datetime import datetime
from exceptions import CustomException

Log_file=f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"Logs")
os.makedirs(log_path,exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_path,Log_file),
    format= "[ %(asctime)s ] %(levelname)s - %(name)s  %(lineno)d - %(message)s",
     level=logging.INFO,

)

if __name__== "__main__":
    logging.info("logging started")
    try:
        a=1/0
    except Exception as e:
        logging.error("Sample error raised")
        raise CustomException(e,sys)