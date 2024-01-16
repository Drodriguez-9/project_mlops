from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastai.tabular.all import *
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Load trained FastAI model
path_to_model = 'trained_model2'
categorical_columns = ['workclass', 'education', 'marital-status', 'occupation', 
                       'relationship', 'race', 'sex', 'native-country']
continuous_columns = ['age', 'fnlwgt', 'education-num', 'capital-gain', 
                      'capital-loss', 'hours-per-week']

# Define your input data model
# This should mirror the features your model was trained on
class InputData(BaseModel):
    age: int = Field(..., alias='age')
    workclass: int = Field(..., alias='workclass')
    fnlwgt: int = Field(..., alias='fnlwgt')
    education: int = Field(..., alias='education')
    education_num: int = Field(..., alias='education-num')
    marital_status: int = Field(..., alias='marital-status')
    occupation: int = Field(..., alias='occupation')
    relationship: int = Field(..., alias='relationship')
    race: int = Field(..., alias='race')
    sex: int = Field(..., alias='sex')
    capital_gain: int = Field(..., alias='capital-gain')
    capital_loss: int = Field(..., alias='capital-loss')
    hours_per_week: int = Field(..., alias='hours-per-week')
    native_country: int = Field(..., alias='native-country')

    class Config:
        allow_population_by_field_name = True

# Define an endpoint for inference
@app.post("/predict")
def predict(data: InputData):
    # Convert input data to DataFrame
    dataframe = pd.read_csv('data/processed/train_data.csv')

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
    input_data = data.dict(by_alias=True)
    input_df = pd.DataFrame([input_data])
    print(input_df)
    # Preprocess the data as per the model's training process
    # Assuming preprocessing similar to training, otherwise adjust as needed
    dl = learn.dls.test_dl(input_df)
    preds = learn.get_preds(dl=dl)
    # Reformat predictions  
    preds = [x.item() for x in preds[0]]
    if preds[0] < 0.5:
        preds = "Less than 50K"
    else:
        preds = "More than 50K"
    return {"prediction": preds}
