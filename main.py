from src.logger import logger
from src.pipeline.train_pipeline import DataIngestionPipeline

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
