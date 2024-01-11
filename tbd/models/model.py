import torch
from fastai.tabular.all import *
model = tabular_learner(df, metrics=accuracy)
class CustomTabularModel(TabularModel):
    def __init__(self, emb_szs, n_cont, out_sz, layers, ps=None, embed_p=0., y_range=None):
        super().__init__(emb_szs, n_cont, out_sz, layers, ps, embed_p, y_range)