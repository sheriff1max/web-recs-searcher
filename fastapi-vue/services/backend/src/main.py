import os

from .schemas import ParamsForPipeline

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from recs_searcher import load_pipeline

import pathlib
import platform
if platform.system() == 'Linux':
    pathlib.WindowsPath = pathlib.PosixPath


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
print(app.PATH_WEIGHTS)

app.MODELS = {
    name: load_pipeline(os.path.join(app.PATH_WEIGHTS, name))
    for name in os.listdir(app.PATH_WEIGHTS)
}
print('Models loaded!')


@app.get('/')
def home():
    return {
        'task_names': os.listdir(app.PATH_WEIGHTS),
    }


@app.post('/')
def predict(params_for_pipeline: ParamsForPipeline):
    model = app.MODELS[params_for_pipeline.task_name]

    df_pred = model.search(params_for_pipeline.text, params_for_pipeline.k)  # pd.DataFrame
    text_array = df_pred.text.values.tolist()
    similarity_array = df_pred.similarity.values.tolist()
    result_list = []
    for i in range(len(text_array)):
        tmp_dict = {
            'text': text_array[i],
            'similarity': round(similarity_array[i], 3)
        }
        result_list.append(tmp_dict)
    return {'result': result_list}
