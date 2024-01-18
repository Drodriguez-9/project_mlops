import pytest
import pandas as pd
from tbd.models.predict_model import predict_tabular_classifier
from pathlib import Path

@pytest.fixture
def processed_data_path():
    return Path('data/processed/')

def test_data_loading(processed_data_path):
    test_data_path = processed_data_path / 'test_data.csv'
    assert test_data_path.exists(), "Test data file does not exist"
    
    # Test if the function can load data without raising an error
    try:
        predicted_classes = predict_tabular_classifier(str(test_data_path))
    except Exception as e:
        pytest.fail(f"Unexpected error occurred while loading data: {e}")

def test_data_preprocessing(processed_data_path):
    # This test would require more detailed knowledge about the expected preprocessing results

def test_model_prediction(processed_data_path):
    test_data_path = processed_data_path / 'test_data.csv'
    predicted_classes = predict_tabular_classifier(str(test_data_path))

    assert isinstance(predicted_classes, list), "Predicted classes should be a list"
    assert all(isinstance(pc, str) for pc in predicted_classes), "All predicted classes should be strings"

def test_incorrect_data_path():
    incorrect_path = 'non_existent_path.csv'
    with pytest.raises(FileNotFoundError):
        predict_tabular_classifier(incorrect_path)