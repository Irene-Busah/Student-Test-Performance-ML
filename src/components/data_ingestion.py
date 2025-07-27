"""
data_ingestion.py
====================

Implements the data ingestion components
"""


# libraries
from src.logger import logger
from src.entity import DataIngestionConfig
import pandas as pd


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    # method to load the data
    def load_data(self):
        data = pd.read_csv(self.config.local_data_file_path)

        logger.info(f"Loading the Data from the local directory")

        logger.info(data.shape)

