import pandas as pd
import sys
import os
from src.logger import logging
from src.data_access.proj1_data import Proj1Data
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact 
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self, config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = config
        except Exception as e:
            raise CustomException(e, sys) from e
    
    def export_data(self) -> pd.DataFrame:
        try:
            logging.info("Exporting data from mongodb")
            data = Proj1Data()
            df = data.export_collection_as_dataframe(self.data_ingestion_config.collection_name)
            dir_name = os.path.dirname(self.data_ingestion_config.data_file_path)
            os.makedirs(dir_name, exist_ok=True)
            logging.info(f'storing extracted data into {dir_name}')
            df.to_csv(self.data_ingestion_config.data_file_path, index=False, header=True)
            logging.info("Data export completed successfully.")
            return df
        except Exception as e:
            logging.error(f"Error occurred while exporting data: {e}")
            raise CustomException(e, sys)
    
    def train_test_split(self,data:pd.DataFrame):
        logging.info("Splitting data into train and test sets")
        try:
            train_df, test_df = train_test_split(data, test_size=self.data_ingestion_config.train_test_split_ratio, random_state=42)
            logging.info("Train and test split completed successfully.")
            train_df.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_df.to_csv(self.data_ingestion_config.test_file_path, index=False, header=True)
            logging.info("Train and test data saved successfully.")

        except Exception as e:
            logging.error(f"Error occurred while splitting data: {e}")
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Initiating data ingestion")
            df = self.export_data()
            self.train_test_split(df)
            data_ingestion_artifacts = DataIngestionArtifact(train_file_path=self.data_ingestion_config.training_file_path,
                                                              test_file_path=self.data_ingestion_config.test_file_path)
            logging.info(f"Data ingestion artifacts created: {data_ingestion_artifacts}")
            return data_ingestion_artifacts
        
        except Exception as e:
            logging.error(f"Error occurred while initiating data ingestion: {e}")
            raise CustomException(e, sys)


