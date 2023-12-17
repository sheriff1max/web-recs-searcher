from typing import Optional
import os
import pandas as pd

from .schemas import ParamsForPipeline
from .utils import parse_pipeline_name

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {
        'list_task_names': os.listdir('src/pipelines'),
    }


@app.post('/')
def predict(params_for_pipeline: ParamsForPipeline):
    # df_pred = ...
    # return {
    #     'text': df_pred.name.values,
    #     'similarity': df_pred.similarity.values,
    # }
    print(params_for_pipeline)
    return {
        'text': ['Iphone 6', 'Iphone 13', 'Iphone 5s', 'Iphone 12'],
        'similarity': [0.00094, 0.00098, 0.0102, 0.0105],
    }
