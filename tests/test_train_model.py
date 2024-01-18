import os
import pytest
from tbd.models.train_model import train_tabular_classifier
import pandas as pd
from tests import _PATH_DATA  # Import the data path
from fastai.tabular.all import accuracy

@pytest.fixture
def setup_data():
    train_data = pd.read_csv(os.path.join(_PATH_DATA, 'processed/train_data.csv'))
    test_data = pd.read_csv(os.path.join(_PATH_DATA, 'processed/test_data.csv'))
    return train_data, test_data

train_data_file = os.path.join(_PATH_DATA, 'processed/train_data.csv')

@pytest.mark.skipif(not os.path.exists(train_data_file), reason="Train data file not found")
def test_data_loading(setup_data):
    train_data, test_data = setup_data
    assert not train_data.empty
    assert not test_data.empty
    assert 'income' in train_data.columns

@pytest.mark.skipif(not os.path.exists(train_data_file), reason="Train data file not found")
def test_train_tabular_classifier(setup_data):
    train_data, _ = setup_data
    trained_model = train_tabular_classifier(train_data_file, 'income', 
                                             ['workclass', 'education', 'marital-status', 'occupation', 
                                              'relationship', 'race', 'sex', 'native-country'],
                                             ['age', 'fnlwgt', 'education-num', 'capital-gain', 
                                              'capital-loss', 'hours-per-week'],
                                              accuracy)
    assert trained_model is not None