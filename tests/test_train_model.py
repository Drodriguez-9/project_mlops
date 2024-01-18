import pytest
from tbd.models.train_model import train_tabular_classifier
import pandas as pd


@pytest.fixture
def setup_data():
    # Load test data (you might want to use smaller, simplified data for testing)
    train_data = pd.read_csv('data/processed/train_data.csv')
    test_data = pd.read_csv('data/processed/test_data.csv')
    return train_data, test_data

def test_data_loading(setup_data):
    train_data, test_data = setup_data
    # Test if data is loaded correctly (e.g., not empty, correct columns)
    assert not train_data.empty
    assert not test_data.empty
    assert 'income' in train_data.columns

def test_train_tabular_classifier(setup_data):
    train_data, _ = setup_data
    # Test the training function
    trained_model = train_tabular_classifier('data/processed/train_data.csv', 'income', 
                                             ['workclass', 'education', 'marital-status', 'occupation', 
                                              'relationship', 'race', 'sex', 'native-country'],
                                             ['age', 'fnlwgt', 'education-num', 'capital-gain', 
                                              'capital-loss', 'hours-per-week'],
                                              accuracy)
    # Check if the model is trained (e.g., by checking if a model file is created or if the model object is not None)
    assert trained_model is not None