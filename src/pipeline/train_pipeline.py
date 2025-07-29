"""
train_pipeline.py
============================

Implements the machine learning pipelines
"""


# libraries
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTraining

from src.config import ConfigurationManager
from src.logger import logger


class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.load_data()


class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfigurationManager()

        data_transformation_config = config.get_data_transformation_config()
        data_transform = DataTransformation(config=data_transformation_config)

        data_transform.rename_data_columns()
        data_transform.encode_categorical_columns()
        data_transform.splitting_data()


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()

        model_training_config = config.get_model_training_config()
        model_training = ModelTraining(config=model_training_config)

        model_training.train_model()

