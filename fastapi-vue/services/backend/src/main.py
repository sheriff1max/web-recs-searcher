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

    return {
        'result': [
            {'text': 'Iphone 11', 'similarity': 0.55},
            {'text': 'Iphone 12', 'similarity': 0.74},
        ]
    }

    df_pred = ...  # pd.DataFrame
    text_array = df_pred.text.values
    similarity_array = df_pred.similarity.values

    result_list = []
    for i in range(len(text_array)):
        tmp_dict = {'text': text_array[i], 'similarity': similarity_array[i]}
        result_list.append(tmp_dict)

    return {'result': result_list}
