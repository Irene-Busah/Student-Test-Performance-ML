from src.logger import logger
from src.pipeline.train_pipeline import DataIngestionPipeline, DataTransformationPipeline, ModelTrainingPipeline

from src.pipeline.predict_pipeline import ModelEvaluationPipeline

logger.info("Logging Setup Completed Successfully")


# ====================================== Data Ingestion ======================================
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e


# ==================================== Data Transformation ====================================
STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e



# ==================================== Model Training ====================================
STAGE_NAME = "Model Training Stage"

try:
    logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
    obj = ModelTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e



# ==================================== Model Training ====================================
STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
    obj = ModelEvaluationPipeline()
    obj.initiate_model_evaluation()
    logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e


logger.info("Student Test Performance Model Completed")
