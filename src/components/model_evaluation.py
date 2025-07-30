"""
model_evaluation.py
====================

Implements the model testing functionality
"""

# importing the relevant libraries
from urllib.parse import urlparse
from src.logger import logger
from src.entity import ModelEvaluationConfig
import pandas as pd
import numpy as np
import mlflow

from sklearn.linear_model import ElasticNet
import json
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/i.busah/Student-Test-Performance-ML.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="i.busah"
os.environ["MLFLOW_TRACKING_PASSWORD"]="71f1c7abadfdc87c2c2d63a2e5527cea4f09d895"


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    

    # defining the method to evaluate the model
    def evaluate_model(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rmse, mae, r2

    # defining the method to log the model to mlflow
    def log_to_mlflow(self):
        """Logs the model performance to mlflow"""

        test_data = pd.read_csv(self.config.test_data_filepath)
        model = joblib.load(self.config.model_name)

        x_test = test_data.drop(columns=[self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]

        # setting the mlflow tracking
        mlflow.set_tracking_uri(uri=self.config.mflow_uri)
        experiment_name = "Student-Performance-Experiment"

        try:
            experiment = mlflow.get_experiment_by_name(name=experiment_name)
            if experiment is None:
                mlflow.create_experiment(experiment_name)
            mlflow.set_experiment(experiment_name)
        
        except Exception as e:
            raise e

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run(run_name='student-performance') as run:
            y_pred = model.predict(x_test)

            (rmse, mae, r2) = self.evaluate_model(y_test, y_pred)

            # saving the metrics 
            scores = {"rmse": rmse, "mae": mae, "r2_score": r2}

            logger.info(f"Model Evaluation Completed - {scores}")

            with open(self.config.metrics_filename, 'w') as file:
                json.dump(scores, file, indent=4)
            
            logger.info(f"Metrics JSON file saved at {file.name}")

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2_score", r2)
            
            # Save model locally
            local_model_path = self.config.model_name
            joblib.dump(model, local_model_path)

            # Log model as artifact
            try:
                mlflow.log_artifact(local_model_path, artifact_path="model")
                logger.info(f"Model saved and logged as artifact at {local_model_path}")
            except Exception as e:
                logger.error(f"Failed to log model artifact: {e}")
                raise e

            # Log metrics file as artifact
            mlflow.log_artifact(self.config.metrics_filename, artifact_path="metrics")

        
        logger.info("MLflow Experiment Logging Complete")




