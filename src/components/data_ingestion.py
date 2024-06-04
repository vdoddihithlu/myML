import sys
import os
import pandas as pd
from src.logger import logging
from src.exceptions import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionCOnfig:
    train_data_path: str = os.path.join("artifacts","train.csv")
    test_data_path: str = os.path.join("artifacts","test.csv")
    raw_data_path: str = os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_Config = DataIngestionCOnfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Starting to ingest data")
            df=pd.read_csv("notebook\data\population.csv")

            logging.info("train test split")
            train, test = train_test_split(df, test_size=0.2, random_state=42)

            logging.info("makedir")
            os.makedirs(os.path.dirname(self.ingestion_Config.raw_data_path), exist_ok=True)   
      #      os.remove(self.ingestion_Config.raw_data_path)

            logging.info("store raw/test/split data")
            df.to_csv(self.ingestion_Config.raw_data_path)
            train.to_csv(self.ingestion_Config.train_data_path)
            test.to_csv(self.ingestion_Config.test_data_path)

            return(
                self.ingestion_Config.train_data_path, 
                   self.ingestion_Config.test_data_path
                   )


        except Exception as e:
            raise CustomException(e,sys)


if __name__== "__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()