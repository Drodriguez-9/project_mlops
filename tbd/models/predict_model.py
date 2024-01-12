import pandas as pd
import torch
from fastai.tabular.all import *
from pathlib import Path

# Load the trained model
model_path = 'models/trained_model.pth'  # Update with the correct path to your trained model
learn = load_learner(model_path)
categorical_columns = ['workclass', 'education', 'marital-status', 'occupation', 
                       'relationship', 'race', 'sex', 'native-country']
continuous_columns = ['age', 'fnlwgt', 'education-num', 'capital-gain', 
                      'capital-loss', 'hours-per-week']
def predict_tabular_classifier(data_path):
    # Load the new data for prediction
    new_data = pd.read_csv(data_path)

    # Ensure the same preprocessing steps as during training
    procs = [Categorify, FillMissing, Normalize]
    to = TabularPandas(new_data, procs=procs, cat_names=categorical_columns, cont_names=continuous_columns)

    # Use the trained model to make predictions
    predictions, _ = learn.get_preds(dl=to.dataloaders())

    # Convert the predictions to human-readable form (e.g., class labels)
    predicted_classes = [learn.dls.categorify.decodes(to.dls.categorify.decode(o))[0] for o in predictions]

    return predicted_classes

if __name__ == "__main__":
    data_to_predict_path = 'data/processed/test_data.csv'  # Update with the path to your new data
    predicted_classes = predict_tabular_classifier(data_to_predict_path)

    # Do something with the predicted classes, e.g., save to a file or print them
    print(predicted_classes)
