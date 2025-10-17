import sys
from src.logger import logging
from src.exception import CustomException

try:
    a = 3/'451d3'
except Exception as e:
    logging.error("Error occurred", exc_info=True)
    raise CustomException("Custom error message", sys) from e