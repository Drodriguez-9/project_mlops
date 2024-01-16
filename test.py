from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastai.tabular.all import *
import pandas as pd
# path = 'data/processed/train_data.csv'
# dataframe = pd.read_csv(path)
# data = dataframe
# # Define the splits (here we're using a random split for simplicity)
# splits = RandomSplitter(valid_pct=0.2)(range_of(data))

# # Preprocess the data
# procs = [Categorify, FillMissing, Normalize]

# # Define the TabularPandas object
# to = TabularPandas(data, procs=procs, cat_names=categorical_columns, cont_names=continuous_columns,
#                     y_names=target_column, splits=splits)

# # Create a DataLoaders object
# dls = to.dataloaders(bs=config.hyperparameters.batch_size)
# model.load('models/trained_model.pth')
    # Convert input data to DataFrame
dataframe = pd.read_csv('data/processed/train_data.csv')
path_to_model = 'trained_model2'
categorical_columns = ['workclass', 'education', 'marital-status', 'occupation', 
                       'relationship', 'race', 'sex', 'native-country']
continuous_columns = ['age', 'fnlwgt', 'education-num', 'capital-gain', 
                      'capital-loss', 'hours-per-week']
# Preprocess the data
procs = [Categorify, FillMissing, Normalize]
# Define the TabularPandas object
to = TabularPandas(dataframe, procs=procs, cat_names=categorical_columns, cont_names=continuous_columns,
                    y_names='income')

# Create a DataLoaders object
dls = to.dataloaders(bs=1)

# Define the learner
learn = tabular_learner(dls, metrics=accuracy)
learn.load(path_to_model)

input_df = pd.read_csv('data/processed/test_data.csv')
# Preprocess the data as per the model's training process
# Assuming preprocessing similar to training, otherwise adjust as needed
dl = learn.dls.test_dl(input_df)
preds = learn.get_preds(dl=dl)
# Reformat predictions
preds = [x.item() for x in preds[0]]
print(preds)
# model = tabular_learner(dl, n_out=2, metrics=accuracy, LossMetrics=CrossEntropyLossFlat())
# model.load(path_to_model)
# Get prediction from model