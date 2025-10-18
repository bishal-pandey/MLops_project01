from dataclasses import dataclass
import os
import sys
from src.components.data_transformation import DataTransformation
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from src.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact, DataTransformationArtifact

# @dataclass
# class DataIngestionArtifact:
#     train_file_path: str = 'artifact/10_18_2025_17_10_13/data_ingestion/train.csv'
#     test_file_path: str = 'artifact/10_18_2025_17_10_13/data_ingestion/test.csv'


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.data_transformation_config = DataTransformationConfig()

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

    def start_data_validation(self, data_ingestion_artifacts: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            logging.info("Enter into data validation in training pipeline")
            data_validation = DataValidation(config=self.data_validation_config,data_ingestion_artifact=data_ingestion_artifacts)
            data_validation_artifacts = data_validation.initiate_data_validation()
            logging.info(f"perform data validation")
            return data_validation_artifacts
        
        except Exception as e:
            logging.error(f"Error occurred while starting data validation in training pipeline: {e}")
            raise CustomException(e, sys)
        
    def start_data_transformation(self, data_ingestion_artifacts:DataIngestionArtifact,data_validation_artifacts:DataValidationArtifact):
        try:
            logging.info("Enter into data transformation in training pipeline")
            data_transformation = DataTransformation(data_ingestion_artifacts,data_validation_artifacts,self.data_transformation_config)

            data_transformation_artifacts = data_transformation.initiate_data_transformation()
            logging.info(f"Data transformation completed")
            return data_transformation_artifacts

        except Exception as e:
            logging.error(f"Error occurred while starting data transformation in training pipeline: {e}")
            raise CustomException(e, sys)

    def run_pipeline(self):
        try:
            logging.info("Enter run pipeline in training pipeline")

            data_ingestion_artifacts = self.start_data_ingestion()
            # data_ingestion_artifacts = DataIngestionArtifact()
            data_validation_artifacts = self.start_data_validation(data_ingestion_artifacts)
            data_transformation_artifacts = self.start_data_transformation(data_ingestion_artifacts, data_validation_artifacts)


        except Exception as e:
            logging.error(f"Error occurred while running training pipeline: {e}")
            raise CustomException(e, sys)