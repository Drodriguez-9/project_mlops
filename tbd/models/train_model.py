import pandas as pd
import warnings
from fastai.tabular.all import *


warnings.filterwarnings('ignore', category=UserWarning)
from omegaconf import OmegaConf
# loading
config = OmegaConf.load('config/hyperparameters.yaml')
seed = 42
def train_tabular_classifier(path, target_column, categorical_columns, continuous_columns, metric):
    # Load the data
    dataframe = pd.read_csv(path)
    data = dataframe
    # Define the splits (here we're using a random split for simplicity)
    splits = RandomSplitter(valid_pct=0.2, seed = seed)(range_of(data))

    # Preprocess the data
    procs = [Categorify, FillMissing, Normalize]
    
    # Define the TabularPandas object
    to = TabularPandas(data, procs=procs, cat_names=categorical_columns, cont_names=continuous_columns,
                       y_names=target_column, splits=splits)
    
    # Create a DataLoaders object
    dls = to.dataloaders(bs=config.hyperparameters.batch_size)
    
    # Define the learner
    learn = tabular_learner(dls, metrics=metric)

    # Train the model
    learn.fit_one_cycle(config.hyperparameters.epochs)

    # Return the trained learner
    torch.save(learn.model, 'models/trained_model.pth')
    return learn
target_column = 'income'
categorical_columns = ['workclass', 'education', 'marital-status', 'occupation', 
                       'relationship', 'race', 'sex', 'native-country']
continuous_columns = ['age', 'fnlwgt', 'education-num', 'capital-gain', 
                      'capital-loss', 'hours-per-week']

#Usage:
trained_model = train_tabular_classifier('data/processed/train_data.csv', target_column, categorical_columns, continuous_columns, accuracy)
