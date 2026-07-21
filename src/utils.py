# src/utils.py
import logging
import warnings
import numpy as np
import pandas as pd
from typing import Callable, List, Tuple, Union

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(path: str) -> pd.DataFrame:
    """
    Load data from a CSV file.

    This function attempts to load data from a CSV file at the specified path.
    If the file does not exist or cannot be loaded, it raises a FileNotFoundError.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(path)
        return data
    except FileNotFoundError as e:
        logging.error(f"Failed to load data from {path}: {e}")
        raise

def save_data(df: pd.DataFrame, path: str) -> None:
    """
    Save a DataFrame to a CSV file.

    This function saves the specified DataFrame to a CSV file at the specified path.
    If the file cannot be saved, it raises a PermissionError.

    Args:
        df (pd.DataFrame): DataFrame to save.
        path (str): Path to the CSV file.
    """
    try:
        df.to_csv(path, index=False)
    except PermissionError as e:
        logging.error(f"Failed to save data to {path}: {e}")
        raise

def check_nan(df: pd.DataFrame) -> Tuple[int, int]:
    """
    Check for missing values in a DataFrame.

    This function returns the number of rows and columns with missing values.

    Args:
        df (pd.DataFrame): DataFrame to check.

    Returns:
        Tuple[int, int]: Number of rows and columns with missing values.
    """
    nan_count = df.isnull().sum()
    logging.info(f"Missing values: {nan_count}")
    return nan_count.sum(), nan_count.shape[0]

def check_infinity(df: pd.DataFrame) -> Tuple[int, int]:
    """
    Check for infinity values in a DataFrame.

    This function returns the number of rows and columns with infinity values.

    Args:
        df (pd.DataFrame): DataFrame to check.

    Returns:
        Tuple[int, int]: Number of rows and columns with infinity values.
    """
    infinity_count = df.isin([np.inf, -np.inf]).sum()
    logging.info(f"Infinity values: {infinity_count}")
    return infinity_count.sum(), infinity_count.shape[0]

def warn_deprecation(message: str, category: str = UserWarning) -> None:
    """
    Warn about deprecated functionality.

    This function raises a UserWarning about deprecated functionality.

    Args:
        message (str): Warning message.
        category (str): Warning category (default: UserWarning).
    """
    warnings.warn(message, category)