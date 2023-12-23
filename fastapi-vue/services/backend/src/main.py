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

app.PATH_WEIGHTS = None
for root, dirs, files in os.walk('./'):
    for dir in dirs:
        if 'weights' == dir:
            app.PATH_WEIGHTS = os.path.join(root, 'weights')
    if app.PATH_WEIGHTS:
        break

app.MODELS = {
    name: load_pipeline(os.path.join(app.PATH_WEIGHTS, name))
    for name in os.listdir(app.PATH_WEIGHTS)
}

@app.get('/')
def home():
    return {
        'list_task_names': os.listdir(app.PATH_WEIGHTS),
    }


@app.post('/')
def predict(params_for_pipeline: ParamsForPipeline):

    model = app.MODELS[params_for_pipeline.task_name]

    df_pred = model.search(params_for_pipeline.text, params_for_pipeline.k)  # pd.DataFrame
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
