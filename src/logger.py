"""
logger.py
==========

Implements the custom logging
"""

# importing the necessary libraries
# import logging
# import os
# from datetime import datetime


# LOG_FILE = F"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# os.makedirs(logs_path, exist_ok=True)

# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )


# if __name__ == '__main__':
#     logging.info("Logging Started Successfully!")



import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("wine_quality_project_logger")

