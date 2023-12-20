from typing import Optional
import os
import pandas as pd

from .schemas import ParamsForPipeline
from .utils import parse_pipeline_name

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from recs_searcher import load_pipeline


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.PATH_WEIGHTS = os.path.join('src', 'models', 'weights')
app.MODEL_NAME = 'Города России.pkl'
app.MODEL = load_pipeline(app.PATH_WEIGHTS, app.MODEL_NAME)

@app.get('/')
def home():
    return {
        'list_task_names': os.listdir(app.PATH_WEIGHTS),
    }


@app.post('/')
def predict(params_for_pipeline: ParamsForPipeline):

    # return {
    #     'result': [
    #         {'text': 'Iphone 11', 'similarity': 0.55},
    #         {'text': 'Iphone 12', 'similarity': 0.74},
    #     ]
    # }
    if params_for_pipeline.task_name == app.MODEL_NAME:
        pass
    else:
        app.MODEL = load_pipeline(app.PATH_WEIGHTS, params_for_pipeline.task_name)

    df_pred = app.MODEL.search(params_for_pipeline.text, params_for_pipeline.k)  # pd.DataFrame
    text_array = df_pred.name.values
    similarity_array = df_pred.similarity.values

    result_list = []
    for i in range(len(text_array)):
        tmp_dict = {
            'text': text_array[i],
            'similarity': float(similarity_array[i])
        }
        result_list.append(tmp_dict)
    return {'result': result_list}
