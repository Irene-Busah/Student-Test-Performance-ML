"""
utils.py
==============

Implements the common functions needed in the project
"""


# libraries
import os
import yaml
from src.logger import logger
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
# from typing import Any


# function to read yaml file
@ensure_annotations
def read_yaml(filepath: Path) -> ConfigBox:
    """Reads the yaml files with the parameters"""

    try:
        with open(filepath) as file:
            content = yaml.safe_load(file)

            logger.info(f"Successfully Loaded the YAML file: {file}")

            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty or not found")
    except Exception as e:
        raise e


# function to create directories
@ensure_annotations
def create_directories(directory_name: list, verbose=True):
    """Creates the different directories"""

    for path in directory_name:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"Directory Created Successfully - {path}")
