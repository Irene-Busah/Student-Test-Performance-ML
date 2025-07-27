"""
train_pipeline.py
============================

Implements the machine learning pipelines
"""


# libraries
from src.components.data_ingestion import DataIngestion

from src.config import ConfigurationManager
from src.logger import logger

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.load_data()

if __name__ == '__main__':
    try:
        logger.info(f'----------------- Stage [{STAGE_NAME}] Started -----------------')
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
    
    except Exception as e:
        logger.exception(e)
        raise e

