import json
import pandas as pd
import os
import sys

from src.logger import logging
from src.exception import CustomException
from src.utils.main_utils import read_yaml_file
from src.entity.artifact_entity import DataValidationArtifact,DataIngestionArtifact
from src.entity.config_entity import DataValidationConfig
from src.constants import SCHEMA_FILE_PATH


class DataValidation:
    def __init__(self, config: DataValidationConfig, data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.data_validation_config = config
            self.data_ingestion_artifact = data_ingestion_artifact
            self._schema_path = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise CustomException(e,sys)
    
    def validate_number_of_columns(self, df:pd.DataFrame):
        try:
            logging.info("Validating number of columns")
            status = len(df.columns) == len(self._schema_path['columns'])
            logging.info(f"Number of columns validation status: {status}")

            return status
        except Exception as e:
            raise CustomException(e,sys)
    
    def is_column_exist(self,df: pd.DataFrame):
        try:
            missing_columns = []
            status = True
            logging.info("Validating if all columns exist")
            for column in self._schema_path['columns']:
                
                if list(column.keys())[0] not in df.columns:
                    missing_columns.append(column)
                    status = False
            if not status:
                logging.info(f"Missing columns: {missing_columns}")

            logging.info(f"Column exists validation status: {status}")
            return status
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_validation(self):
        try:
            validation_msg = ''
            logging.info("Initiating data validation")
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            if not self.validate_number_of_columns(train_df):
                validation_msg += "Number of columns in train dataframe is incorrect. " 
            else:
                logging.info("Number of columns in train dataframe is correct.")

            if not self.is_column_exist(train_df):
                validation_msg += "Missing columns in train dataframe. "
            else:
                logging.info("All columns are present in train dataframe.")
            

            if not self.validate_number_of_columns(test_df):
                validation_msg += "Number of columns in test dataframe is incorrect. "
            else:
                logging.info("Number of columns in test dataframe is correct.")

            if not self.is_column_exist(test_df):
                validation_msg += "Missing columns in test dataframe. "
            else:
                logging.info("All columns are present in test dataframe.")

            if validation_msg:
                validation_status = False
                logging.error(f"Data validation errors found: {validation_msg}")
            else:
                validation_status = True
                logging.info("Data validation successful.")

            data_validation_artifact = DataValidationArtifact(
                validation_status = validation_status,
                message = validation_msg,
                report_file_path=self.data_validation_config.report_file_path
            )

            report_dir = os.path.dirname(self.data_validation_config.report_file_path)
            os.makedirs(report_dir, exist_ok=True)

            validation_report = {
                "validation_status": validation_status,
                "message": validation_msg,
            }

            with open(self.data_validation_config.report_file_path, 'w') as report_file:
                json.dump(validation_report, report_file,indent=5)

            logging.info('Data validation artifact created and saved to json successfully.')
            logging.info("Data validation completed")
    
            return data_validation_artifact

        except Exception as e:
            raise CustomException(e,sys)

