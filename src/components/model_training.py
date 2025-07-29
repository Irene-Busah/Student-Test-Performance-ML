"""
model_training.py
====================

Implements the model training
"""


# libraries
from src.logger import logger
from src.entity import ModelTrainingConfig
import pandas as pd

from sklearn.linear_model import ElasticNet
import joblib
import os


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
    
    # method to train the model
    def train_model(self):
        """Trains the student performance model"""

        logger.info(f"Model Training Started")

        # loading the training and testing data
        train_data = pd.read_csv(self.config.train_data_filepath)
        test_data = pd.read_csv(self.config.test_data_filepath)

        # getting the dependent and target variables
        x_train = train_data.drop(columns=[self.config.target_column], axis=1)
        x_test = test_data.drop(columns=[self.config.target_column], axis=1)

        y_train = train_data[[self.config.target_column]]
        y_test = test_data[[self.config.target_column]]

        # training the model
        model = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            fit_intercept=self.config.fit_intercept,
            max_iter=self.config.max_iter,
            selection=self.config.selection,
            random_state=self.config.random_state
        )

        # fitting the model
        model.fit(x_train, y_train)

        # saving the model
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))

        logger.info(f"Model Training Completed & Saved: {os.path.join(self.config.root_dir, self.config.model_name)}")


    
