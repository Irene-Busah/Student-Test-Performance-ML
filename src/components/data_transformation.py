"""
data_transformation.py
====================

Implements the data transformation components
"""


# libraries
from src.logger import logger
from src.entity import DataTransformationConfig
import pandas as pd

from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    # method to rename the data columns
    def rename_data_columns(self):
        """Renames the data columns"""
        data = pd.read_csv(self.config.data_filepath)


        # renaming the columns
        data = data.rename(
            columns={
                "race/ethnicity": "race_ethnicity",
                "parental level of education": "parental_level_of_education",
                "test preparation course": "test_preparation_course",
                "math score": "math_score",
                "reading score": "reading_score",
                "writing score": "writing_score"
            }
        )

        data['total_score'] = (data['math_score'] + data['reading_score'] + data['writing_score'])

        data['average_score'] = data["total_score"] / 3

        data.to_csv(self.config.cleaned_data_filepath, index=False)


        logger.info(f"Renaming Data Columns Completed")
    

    # method to encode the non-numeric columns
    def encode_categorical_columns(self):
        """Encodes the categorical columns"""
        data = pd.read_csv(self.config.cleaned_data_filepath)

        categorical_columns = ['race_ethnicity', 'parental_level_of_education', 'test_preparation_course', 'gender', 'lunch']

        encoded_data = pd.get_dummies(data=data, columns=categorical_columns, prefix=categorical_columns, drop_first=True, dtype=int)

        # saving the encoded data
        encoded_data.to_csv(self.config.cleaned_data_filepath, index=False)

        logger.info(f"Categorical Columns Successfully Encoded")

        

    def splitting_data(self):
        """The method splits the data for training and testing the model"""
        data = pd.read_csv(self.config.cleaned_data_filepath)

        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(self.config.train_data_filepath, index=False)
        test.to_csv(self.config.test_data_filepath, index=False)

        logger.info("Data Splitting Completed")
    

