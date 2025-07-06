import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass 
# Data class to hold configuration for data ingestion
# This class defines the configuration for data ingestion, including paths for raw data, train data, and test data.
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            # Read the dataset from the specified path
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Dataset read as pandas dataframe")

            # Create directories if they do not exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Save the raw data to the specified path
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved at {self.ingestion_config.raw_data_path}")

            # Split the data into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("Train and test sets created")

            # Save the training and testing sets to their respective paths
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True) #index=False means do not write row indices to the file
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info(f"Train data saved at {self.ingestion_config.train_data_path}")
            logging.info(f"Test data saved at {self.ingestion_config.test_data_path}")

            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e, sys)

if  __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
    logging.info("Data Ingestion completed")