

# for mongodb connection
DATABASE_NAME = 'Proj01'
COLLECTION_NAME = 'data'
MONGO_CONNECTION_URL = "MONGODB_URL"   #Environment variable name

PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact"

#data file names
DATA_FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

# for data Ingestion
DATA_INGESTION_COLLECTION_NAME = 'data'
DATA_INGESTION_DIR_NAME = 'data_ingestion'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2
