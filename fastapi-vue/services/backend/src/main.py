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
def predict(params_for_pipeline: ParamsForPipeline, flag_show_interpret: bool = False):
    model = app.MODELS[params_for_pipeline.task_name]

    df_pred = model.search(params_for_pipeline.text, params_for_pipeline.k)  # pd.DataFrame
    text_array = df_pred.text.values.tolist()
    similarity_array = df_pred.similarity.values.tolist()
    search_result_array = []
    for i in range(len(text_array)):
        tmp_dict = {
            'text': text_array[i],
            'similarity': round(similarity_array[i], 3)
        }
        search_result_array.append(tmp_dict)
    
    explain_result_array = []
    if flag_show_interpret:
        max_n_grams = len(text_array[0].split())
        if max_n_grams > 3:
            max_n_grams = 3

        df_pred = model.explain(
            compared_text=params_for_pipeline.text,
            original_text=text_array[0],
            n_grams=(1, max_n_grams),
            k=params_for_pipeline.k,
        )
        text_array = df_pred.text.values.tolist()
        similarity_array = df_pred.similarity.values.tolist()
        for i in range(len(text_array)):
            tmp_dict = {
                'text': text_array[i],
                'similarity': round(similarity_array[i], 3)
            }
            explain_result_array.append(tmp_dict)

    return {
        'search_result_array': search_result_array,
        'explain_result_array': explain_result_array,
    }
