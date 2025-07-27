"""
entity.py
==============

Implements the entities for the various components
"""

# libraries
from src.logger import logger

from dataclasses import dataclass
from pathlib import Path


# data ingestion entity
@dataclass
class DataIngestionConfig:
    root_dir: Path
    local_data_file_path: Path
