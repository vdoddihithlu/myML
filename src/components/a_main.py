import sys

from src.exceptions import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

class temp_main:
    def __init__(self):
        # Initialization code here
        pass

    def call_main(self):
        try:
   
            ingest = DataIngestion()
            train_path, test_path = ingest.initiate_data_ingestion()
            logging.info("Train path is {0}".format(train_path))
            logging.info("Test path is {0}".format(test_path))

            process = DataTransformation()
            train_df, test_df = process.innitiate_preprocessing(train_path, test_path)

            

        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj=temp_main()
    obj.call_main()
        
