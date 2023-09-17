from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
import os
import sys
import numpy as np 
from src.utils import save_object

path = r"C:\Users\riate\Documents\Velocity_Data_Science\ml_e2e\notebook\stud.csv"
@dataclass
class DataTransformationConfig():
    preprocessor_object_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation():
    def __init__(self):
        self.preprocessor_object = DataTransformationConfig()

    def generate_preprocessor_object(self):
        try:
            df = pd.read_csv(path)
            numerical_features = ["writing_score", "reading_score"]
            categorical_features =["gender",
                                "race_ethnicity",
                                "parental_level_of_education",
                                "lunch",
                                "test_preparation_course",
                                ]
            
            num_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler(with_mean=False)),
            ])

            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False)),
            ])

            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_features),
                ("cat_pipeline", cat_pipeline, categorical_features),
            ])

            return preprocessor
        
        except Exception as e:
            logging.info(CustomException(e, sys))
            raise CustomException(e, sys)
        
    def initate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("test/train reading completed!")

            preprocessor_obj = self.generate_preprocessor_object()
            
            target_column = "math_score"
            numerical_features = ["writing_score", "reading_score"]
            categorical_features =["gender",
                                "race_ethnicity",
                                "parental_level_of_education",
                                "lunch",
                                "test_preparation_course",
                                ]
            
            input_feature_train_df = train_df.drop(target_column, axis=1)
            input_feature_test_df = test_df.drop(target_column, axis=1)

            target_feature_train = train_df[target_column]
            target_feature_test = test_df[target_column]
            logging.info("Applying feature processing")

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_array = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr,np.array[target_feature_train]]
            test_arr = np.c_[input_feature_test_array, np.array[target_feature_test]]

            logging.info("saved preprocessor object")

            save_object(self.preprocessor_object.preprocessor_object_path,
                        preprocessor_obj)
            
            return(
                train_arr, test_arr, self.preprocessor_object.preprocessor_object_path
            )
        except Exception as e:
            logging.info(CustomException(e, sys))
            raise CustomException(e, sys)
