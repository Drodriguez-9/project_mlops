import pytest
import pandas as pd
from tbd.models.predict_model import predict_tabular_classifier
import os
from tests import _PATH_DATA  # Import the data path

@pytest.fixture
def processed_data_path():
    return os.path.join(_PATH_DATA, 'processed/')

test_data_file = os.path.join(_PATH_DATA, 'processed/test_data.csv')

@pytest.mark.skipif(not os.path.exists(test_data_file), reason="Test data file not found")
def test_data_loading(processed_data_path):
    test_data_path = os.path.join(processed_data_path, 'test_data.csv')
    try:
        predicted_classes = predict_tabular_classifier(test_data_path)
    except Exception as e:
        pytest.fail(f"Unexpected error occurred while loading data: {e}")

# Additional tests ...

@pytest.mark.skipif(not os.path.exists(test_data_file), reason="Test data file not found")
def test_model_prediction(processed_data_path):
    test_data_path = os.path.join(processed_data_path, 'test_data.csv')
    predicted_classes = predict_tabular_classifier(test_data_path)
    assert isinstance(predicted_classes, list)
    assert all(isinstance(pc, str) for pc in predicted_classes)

def test_incorrect_data_path():
    incorrect_path = 'non_existent_path.csv'
    with pytest.raises(FileNotFoundError):
        predict_tabular_classifier(incorrect_path)