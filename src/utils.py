import os
import sys
import dill 
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pickle

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as  e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)
    

def evaluate_models(X_train, y_train ,X_test, y_test, models, params):
    try:
        report = {}
        for model_values, param_values in zip(models.values(), params.values()):
            model = model_values
            param = param_values

            gs = GridSearchCV(model, param, cv=5)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_values] = test_model_score

        return report

    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)
    

def load_model(file_path):
    try:
        with open(file_path,"rb") as f:
            return pickle.load(f)
        
    except CustomException as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)