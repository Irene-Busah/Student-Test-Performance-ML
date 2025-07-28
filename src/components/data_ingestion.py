"""
data_ingestion.py
====================

Implements the data ingestion components
"""


# libraries
from src.logger import logger
from src.entity import DataIngestionConfig
import pandas as pd
import io


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    # method to load the data
    def load_data(self):
        data = pd.read_csv(self.config.local_data_file_path)

        logger.info(f"Loading the Data from the local directory")

        # Capture DataFrame info as a string
        buffer = io.StringIO()
        data.info(buf=buffer)
        info_str = buffer.getvalue()
        buffer.close()

        with open(self.config.Status_file, 'w') as file:
            file.write(f"Data Shape: {data.shape}\n")
            file.write(info_str)

        logger.info(f"Data Summary Saved Successfully")

