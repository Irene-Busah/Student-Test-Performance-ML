"""
config.py
===============

Configs the entities of the pipeline
"""

# libraries
# from src.logger import logger
from src.utils import create_directories, read_yaml
from src.entity import DataIngestionConfig, DataTransformationConfig, ModelTrainingConfig
from pathlib import Path
from box import ConfigBox


# defining constants
PARAM_FILE_PATH = Path('src/params.yaml')
CONFIG_FILE_PATH = Path('src/config.yaml')
SCHEMA_FILE_PATH = Path('src/schema.yaml')


class ConfigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH, params_path=PARAM_FILE_PATH, schema_path=SCHEMA_FILE_PATH):
        self.config = read_yaml(config_path)
        self.param = read_yaml(params_path)
        self.schema = read_yaml(schema_path)
    
        # creating the data ingestion directory
        create_directories([self.config.artifacts_root])
    
    # method to get the data ingestion configuration
    def get_data_ingestion_config(self) -> ConfigBox:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig (
            root_dir=config.root_dir,
            local_data_file_path=config.local_data_file_path,
            Status_file=config.Status_file
        )

        return data_ingestion_config


    def get_data_transformation_config(self) -> ConfigBox:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig (
            root_dir=config.root_dir,
            data_filepath=config.data_filepath,
            cleaned_data_filepath=config.cleaned_data_filepath,
            train_data_filepath=config.train_data_filepath,
            test_data_filepath=config.test_data_filepath
        )

        return data_transformation_config
    
    def get_model_training_config(self) -> ConfigBox:
        config = self.config.model_training
        params = self.param.elastic_net
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            train_data_filepath=config.train_data_filepath,
            test_data_filepath=config.test_data_filepath,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            fit_intercept=params.fit_intercept,
            max_iter=params.max_iter,
            selection=params.selection,
            random_state=params.random_state,
            target_column=schema.name
        )

        return model_training_config

