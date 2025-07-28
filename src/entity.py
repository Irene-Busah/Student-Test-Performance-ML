"""
entity.py
==============

Implements the entities for the various components
"""

# libraries
from dataclasses import dataclass
from pathlib import Path


# data ingestion entity
@dataclass
class DataIngestionConfig:
    root_dir: Path
    local_data_file_path: Path
    Status_file: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_filepath: Path
    cleaned_data_filepath: Path
    train_data_filepath: Path
    test_data_filepath: Path
