import pandas as pd
from fastai.tabular.all import *
# Path: tbd/train_model.py




def train_tabular_classifier(path, target_column, categorical_columns, continuous_columns, metric):
    # Load the data
    dataframe = pd.read_csv(path)
    data = dataframe
    print(dataframe.head(15))
    # Define the splits (here we're using a random split for simplicity)
    splits = RandomSplitter(valid_pct=0.2)(range_of(data))

    # Preprocess the data
    procs = [Categorify, FillMissing, Normalize]
    
    # Define the TabularPandas object
    to = TabularPandas(data, procs=procs, cat_names=categorical_columns, cont_names=continuous_columns,
                       y_names=target_column, splits=splits)
    
    # Create a DataLoaders object
    dls = to.dataloaders(bs=64)
    
    # Define the learner
    learn = tabular_learner(dls, metrics=metric)

    # Train the model
    learn.fit_one_cycle(5)

    # Return the trained learner
    torch.save(learn.model, 'models/trained_model.pth')
    return learn
target_column = 'income'
categorical_columns = ['workclass', 'education', 'marital-status', 'occupation', 
                       'relationship', 'race', 'sex', 'native-country']
continuous_columns = ['age', 'fnlwgt', 'education-num', 'capital-gain', 
                      'capital-loss', 'hours-per-week']

# Example Usage:
trained_model = train_tabular_classifier('data/processed/data.csv', target_column, categorical_columns, continuous_columns, accuracy)