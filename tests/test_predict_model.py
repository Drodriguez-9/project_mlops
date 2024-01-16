import pytest
from tbd.models.predict_model import predict_tabular_classifier
import pandas as pd


TEST_DATA_PATH = 'data/processed/test_data.csv'
TRAINED_MODEL_PATH = 'models/trained_model.pth'

def test_load_data():
    # Test if data loading is successful and the data frame is not empty
    data = pd.read_csv(TEST_DATA_PATH)
    assert not data.empty, "Data loading failed or data is empty"

def test_predict_tabular_classifier():
    # Test if the prediction function returns predictions in the expected format
    predicted_classes = predict_tabular_classifier(TEST_DATA_PATH)
    assert isinstance(predicted_classes, list), "Predictions should be a list"
    assert all(isinstance(cls, str) for cls in predicted_classes), "All predictions should be strings (class labels)"
