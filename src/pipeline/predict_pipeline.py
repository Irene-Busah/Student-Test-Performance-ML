"""
predict_pipeline.py
============================

Implements the model evaluation pipeline
"""


# libraries
from src.components.model_evaluation import ModelEvaluation

from src.config import ConfigurationManager
from src.logger import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()

        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_to_mlflow()

