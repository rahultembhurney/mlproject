from src.logger import logging
from src.exception import CustomException
import pandas as pd 
from sklearn.model_selection import train_test_split
import sys
import os
from dataclasses import dataclass

@dataclass
class DataIngestionConfig():
    train_path = os.path.join("artifacts", "train.csv")
    test_path = os.path.join("artifacts", "test.csv")
    data_path = os.path.join("artifacts", "raw.csv")

class DataIngestion():
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Creating artifacts")
        os.makedirs(os.path.dirname(self.data_ingestion_config.train_path),\
                    exist_ok=True)
        logging.info("Reading file")
        df = pd.read_csv(r"C:\Users\riate\Documents\Velocity_Data_Science\ml_e2e\notebook\stud.csv")

        logging.info("Creating raw.csv")
        df.to_csv(self.data_ingestion_config.data_path, index=False,\
                  header=True)
        logging.info("raw.csv successfully created")

        logging.info("Creating test and train csv")
        train_data, test_data = train_test_split(df, test_size=0.2)

        logging.info("Creating train.csv")
        train_data.to_csv(self.data_ingestion_config.train_path, \
                          header=True, index=False)
        logging.info("train.csv successfully created")

        logging.info("Creating test.csv")
        test_data.to_csv(self.data_ingestion_config.test_path, \
                          header=True, index=False)
        logging.info("test.csv successfully created")

        return (self.data_ingestion_config.train_path,
                self.data_ingestion_config.test_path)
    

if __name__ == "__main__":
    try:
        obj = DataIngestion()
        trd, tsd = obj.initiate_data_ingestion()
    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)


    