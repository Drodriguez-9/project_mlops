import os
import pandas as pd
from pathlib import Path

# test_your_module.py


def get_training_set():
    # Load the training set from the data folder
    training_set_path = 'data/processed/train_data.csv'
    return pd.read_csv(training_set_path)

def get_testing_set():
    # Load the testing set from the data folder
    testing_set_path = 'data/processed/test_data.csv'
    return pd.read_csv(testing_set_path)


