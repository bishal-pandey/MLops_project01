

# for mongodb connection
import os


DATABASE_NAME = 'Proj01'
COLLECTION_NAME = 'data'
MONGO_CONNECTION_URL = "MONGODB_URL"   #Environment variable name

PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact"
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
TARGET_COLUMN: str = "Response"

#data file names
DATA_FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

# for data Ingestion
DATA_INGESTION_COLLECTION_NAME = 'data'
DATA_INGESTION_DIR_NAME = 'data_ingestion'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2

#for data validation
DATA_VALIDATION_DIR_NAME = 'data_validation'
DATA_VALIDATION_REPORT_FILE_NAME = 'report.yaml'
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")


#for data transformation
DATA_TRANSFORMATION_DIR_NAME = 'data_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = 'transformed_data'
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = 'transformed_objects'
