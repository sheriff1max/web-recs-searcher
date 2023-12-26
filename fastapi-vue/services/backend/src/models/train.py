from recs_searcher import (
    preprocessing,
    models,
    similarity_search,
    dataset,
    augmentation,
)
from recs_searcher import api


SEED = 1
PIPELINE_NAME = 'Компьютерные видеоигры'


if __name__ == '__main__':
    dataset_games = dataset.load_video_games()
    # dataset_city_russia = dataset.load_city_russia()
    dataset = dataset_games

    SPACY_MODEL_NAME = 'en_core_web_md'
    # SPACY_MODEL_NAME = 'ru_core_news_md'
    preprocessing_list = [
        preprocessing.TextLower(),
        preprocessing.RemovePunct(),
        # preprocessing.RemoveNumber(),
        preprocessing.RemoveWhitespace(),
        # preprocessing.RemoveHTML(),
        # preprocessing.RemoveURL(),
        # preprocessing.RemoveEmoji(),

        # preprocessing.RemoveStopwordsSpacy(spacy_model_name=SPACY_MODEL_NAME),
        # preprocessing.LemmatizeSpacy(spacy_model_name=SPACY_MODEL_NAME),
    ]

    model_fasttext = models.FastTextWrapperModel(
        min_count=1,
        vector_size=20,
        window=2,
        sg=1,
        hs=1,
        epochs=70,
        min_n=0,
        seed=SEED,
    )

    # LANGUAGE = 'russian'
    # augmentation_transforms_seed_none = [
    #     augmentation.ChangeSyms(p=0.013, language=LANGUAGE, change_only_alpha=True, seed=None),
    #     augmentation.DeleteSyms(p=0.013, delete_only_alpha=True, seed=None),
    #     augmentation.AddSyms(p=0.013, language=LANGUAGE, seed=None),
    #     augmentation.MultiplySyms(p=0.013, count_multiply=2, multiply_only_alpha=True, seed=None),
    #     augmentation.SwapSyms(p=0.013, seed=None),
    #     augmentation.ChangeSyms(p=0.013, language=LANGUAGE, change_only_alpha=True, seed=None),
    #     augmentation.ChangeSyms(p=0.013, language=LANGUAGE, change_only_alpha=True, seed=None),
    # ]
    # model_transformer = models.SentenceTransformerWrapperModel(
    #     augmentation_transform=augmentation_transforms_seed_none,
    #     batch_size=32,
    #     epochs=3,
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
    pipeline.save('./src/models/weights', PIPELINE_NAME)
