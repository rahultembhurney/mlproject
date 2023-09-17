import os
import sys
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object, evaluate_models

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

@dataclass
class ModelTrainerConfig():
    model_trainer_config = os.path.join("artifacts", "model.pkl")

class ModelTrainer():
    def __init__(self):
        self.model_trainer = ModelTrainerConfig()
    
    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info("split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
                )
            models = {
                "LinearRegression":LinearRegression(),
                "DecisionTreeRegressor":DecisionTreeRegressor(),
            }

            params = {
                "LinearRegression": {},
                "DecisionTreeRegressor": {
                    "criterion": ["squared_error", "friedman_mse",
                                  "absolute_error", "possion"],
                }
            }

            model_report:dict = evaluate_models(X_train,
                                                y_train,
                                                X_test,
                                                y_test, models=models,
                                                params=params)
            
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score <0.6:
                raise CustomException("No best model found")
            
            logging.info("No best model found")

            save_object(self.model_trainer.model_trainer_config,
                        obj=best_model)
            
            predicted = best_model.predict(X_test)
            r2_squared = r2_score(y_test, predicted)
            return r2_squared
        
        except CustomException as e:
            logging.info(CustomException(e, sys))
            raise CustomException(e, sys)
