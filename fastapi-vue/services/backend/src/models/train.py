from recs_searcher import (
    preprocessing,
    models,
    similarity_search,
    augmentation,
)
from recs_searcher import api

import pandas as pd


SEED = 1
PIPELINE_NAME = 'Компьютерные игры'


if __name__ == '__main__':
    dataset_games = pd.read_csv('./datasets/video_games.csv')
    # dataset_exoplanets = pd.read_csv('./datasets/exoplanets.csv')
    # dataset_city_russia = pd.read_csv('./datasets/city_russia.csv')
    # dataset_games = dataset.load_video_games()
    # dataset_exoplanets = dataset.load_exoplanes()
    # dataset_city_russia = dataset.load_city_russia()
    dataset = dataset_games

    preprocessing_list = [
        preprocessing.BaseCleaner(remove_number=False),
        preprocessing.BaseNormalizer(
            'russian',
            remove_stopwords=True,
            number_extract=False,
            lemmatize=True,
        ),
    ]

    model_fasttext = models.FastTextWrapperModel(
        min_count=1,
        vector_size=200,
        window=2,
        sg=1,
        hs=1,
        epochs=70,
        min_n=0,
        seed=SEED,
    )

    # augmentation_transforms_seed_none = [
    #     augmentation.MisspellingAugmentation(
    #         add_syms={'p': 0.01, 'language': 'russian'},
    #         change_syms={'p': 0.01, 'language': 'russian'},
    #         delete_syms={'p': 0.01},
    #         multiply_syms={'p': 0.01},
    #         swap_syms={'p': 0.01},
    #         seed=None,
    #     ),
    # ]
    # model_transformer = models.SentenceTransformerWrapperModel(
    #     augmentation_transform=augmentation_transforms_seed_none,
    #     batch_size=32,
    #     epochs=5,
    #     optimizer_params={'lr': 2e-2},
    # )

    searcher_faiss = similarity_search.FaissSearch

    pipeline = api.Pipeline(
        dataset=dataset.target.values,
        preprocessing=preprocessing_list,
        model=model_fasttext,
        searcher=searcher_faiss,
        verbose=True,
    )
    pipeline.save('weights', PIPELINE_NAME)
