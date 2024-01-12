import os
import pytest
from tests.utils import get_training_set, get_testing_set
import pandas as pd


def test_sets_have_data():
    # Get the training and testing sets
    training_set = get_training_set()
    testing_set = get_testing_set()

    # Check if the DataFrames have any data
    assert not training_set.empty, "Training set is empty."
    assert not testing_set.empty, "Testing set is empty."



def test_sets_equality():
    # Get the training and testing sets
    training_set = get_training_set()
    testing_set = get_testing_set()

    # Check if the union of training and testing sets equals the original dataset
    combined_set = pd.concat([training_set, testing_set], ignore_index=True)
    original_set = pd.read_csv('data/processed/data.csv')  

    assert combined_set.equals(original_set), "Training and testing sets combined do not equal the original dataset."