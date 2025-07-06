import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
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