# Salary classification MLOps 

## Project structure

The directory structure of the project looks like this:

```txt

├── Makefile             <- Makefile with convenience commands like `make data` or `make train`
├── README.md            <- The top-level README for developers using this project.
├── data
│   ├── processed        <- The final, canonical data sets for modeling.
│   └── raw              <- The original, immutable data dump.
│
├── docs                 <- Documentation folder
│   │
│   ├── index.md         <- Homepage for your documentation
│   │
│   ├── mkdocs.yml       <- Configuration file for mkdocs
│   │
│   └── source/          <- Source directory for documentation files
│
├── models               <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks            <- Jupyter notebooks.
│
├── pyproject.toml       <- Project configuration file
│
├── reports              <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures          <- Generated graphics and figures to be used in reporting
│
├── requirements.txt     <- The requirements file for reproducing the analysis environment
|
├── requirements_dev.txt <- The requirements file for reproducing the analysis environment
│
├── tests                <- Test files
│
├── tbd  <- Source code for use in this project.
│   │
│   ├── __init__.py      <- Makes folder a Python module
│   │
│   ├── data             <- Scripts to download or generate data
│   │   ├── __init__.py
│   │   └── make_dataset.py
│   │
│   ├── models           <- model implementations, training script and prediction script
│   │   ├── __init__.py
│   │   ├── model.py
│   │
│   ├── visualization    <- Scripts to create exploratory and results oriented visualizations
│   │   ├── __init__.py
│   │   └── visualize.py
│   ├── train_model.py   <- script for training the model
│   └── predict_model.py <- script for predicting from a model
│
└── LICENSE              <- Open-source license if one is chosen
```

Created using [mlops_template](https://github.com/SkafteNicki/mlops_template),
a [cookiecutter template](https://github.com/cookiecutter/cookiecutter) for getting
started with Machine Learning Operations (MLOps).



Salary classification using Deep Learning library fast.ai
==============================

This repository contains the project work of Team 72 for the DTU course [Machine Learning Operations](https://kurser.dtu.dk/course/02476) for the year 2024.

Team members:

- Dimitris Voukatas s230148
- Diego Rodriguez Gordo s222883
- Welin Mark Hageman S233593
- Pierre Høgenhaug s223730

### Overall goal
The goal of this project is to predict if a person earns more or less than $50k per year using some general data and the deep learning library fast.ai (https://docs.fast.ai/). The overarching goal is twofold: firstly, to gain a comprehensive understanding of diverse MLops facets, and secondly, to produce a project with inherent scalability, enabling seamless integration with various datasets and adaptability for incorporation into diverse projects.

### Framework
We plan to use the deep learning library fast.ai (https://docs.fast.ai/), with a specific focus on the Fast.ai tabular module. This module is intricately crafted to manage structured data and provides a user-friendly API for effortlessly constructing and training machine learning models on tabular datasets.

### How to include the framework
We want to use different fastai's functionalities like TabularDataLoaders, TabularPandas, and the provided preprocessors in order the framework efficiently to handle tabular data, prepares it for model training, and facilitates the creation of data loaders for subsequent use in model training and evaluation.

### Dataset
We plan to utilize a dataset comprising 48.842 data points, encompassing information such as age, workclass, educational level, relationship status, sex, race, and other relevant attributes. The dataset has been sourced from the UC Irvine Machine Learning Repository (https://archive.ics.uci.edu/dataset/2/adult).


Created using [mlops_template](https://github.com/SkafteNicki/mlops_template),
a [cookiecutter template](https://github.com/cookiecutter/cookiecutter) 
