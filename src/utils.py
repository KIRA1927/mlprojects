import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import dill  # Using dill for serialization of complex objects

def save_object(obj, file_path):
    """
    Save an object to a file using pandas serialization.
    
    Parameters:
    obj (object): The object to be saved.
    file_path (str): The path where the object will be saved.
    
    Returns:
    None
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)  # Create directory if it doesn't exist
        with open(file_path, 'wb') as file:
            dill.dump(obj, file)  # Use dill to serialize the object
        logging.info(f"Object saved at {file_path}")
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train,y_train,X_test,y_test,models):
    """
    Evaluate multiple models and return their performance metrics.
    
    Parameters:
    X (np.ndarray): Feature matrix.
    y (np.ndarray): Target vector.
    models (dict): Dictionary of model names and their instances.
    
    Returns:
    dict: Dictionary containing model names and their R2 scores.
    """
    try:
        report = {}
        for i in range(len(list(models))):

            model = list(models.values())[i]

            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_test)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_test, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        
        return report
        
    except Exception as e:
        raise CustomException(e, sys)