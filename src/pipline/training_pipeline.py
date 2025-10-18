import os
import sys
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Enter start data ingestion in training pipeline")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info(f"Got train and test data")
            return data_ingestion_artifacts
        except Exception as e:
            logging.error(f"Error occurred while starting data ingestion in training pipeline: {e}")
            raise CustomException(e, sys)
    
    def run_pipeline(self):
        try:
            logging.info("Enter run pipeline in training pipeline")
            data_ingestion_artifacts = self.start_data_ingestion()
        except Exception as e:
            logging.error(f"Error occurred while running training pipeline: {e}")
            raise CustomException(e, sys)