import pytest

from tbd.models.train_model import train_tabular_classifier
import os
import pandas as pd


def test_data_loading():
    path = 'data/processed/train_data.csv'
    target_column = 'income'
    categorical_columns = []
    continuous_columns = []
    learner = train_tabular_classifier(path, target_column, categorical_columns, continuous_columns, accuracy)
    assert learner.dls.train.dataset is not None
    assert learner.dls.valid.dataset is not None

def test_model_training():
    path = 'data/processed/train_data.csv'
    target_column = 'income'
    categorical_columns = []
    continuous_columns = []
    learner = train_tabular_classifier(path, target_column, categorical_columns, continuous_columns, accuracy)

    assert learner.model is not None

def test_model_saving():
    path = 'data/processed/train_data.csv'
    target_column = 'income'
    categorical_columns = ['workclass', 'education', 'marital-status', 'occupation', 
                           'relationship', 'race', 'sex', 'native-country']
    continuous_columns = ['age', 'fnlwgt', 'education-num', 'capital-gain', 
                          'capital-loss', 'hours-per-week']

    learner = train_tabular_classifier(path, target_column, categorical_columns, continuous_columns, accuracy)

    assert 'trained_model2.pth' in os.listdir('models/')