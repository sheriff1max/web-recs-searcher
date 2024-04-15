"""
cd fastapi-vue/services/backend
python ./src/models/train.py
"""


from recs_searcher import (
    dataset,  # учебные датасеты
    preprocessing,  # предобработка текста
    embeddings,  # преобразование текста в эмбеддинги
    similarity_search,  # быстрые поисковики в пространстве эмбеддингов
    augmentation,  # аугментация текста для валидации пайплайнов
    explain,  # интерпретация сходства двух текстов
)
from recs_searcher import api  # Пайплайн


SEED = 1
PIPELINE_NAME = 'Города России'


if __name__ == '__main__':
    # tmp_dataset = dataset.load_video_games()
    tmp_dataset = dataset.load_city_russia()

    # SPACY_MODEL_NAME = 'en_core_web_md'
    SPACY_MODEL_NAME = 'ru_core_news_md'
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

    model_count_vectorizer_char = embeddings.CountVectorizerWrapperEmbedding(
        analyzer='char_wb',
        ngram_range=(2, 2),
    )

    # augmentation_transforms_seed_none = [
    #     augmentation.CharAugmentation(
    #         action='insert',
    #         unit_prob=1.0,
    #         min_aug=1,
    #         max_aug=2,
    #         mult_num=2,
    #         seed=None,
    #     ),
    #     augmentation.CharAugmentation(
    #         action='delete',
    #         unit_prob=1.0,
    #         min_aug=1,
    #         max_aug=2,
    #         mult_num=2,
    #         seed=None,
    #     ),
    # ]
    # model_sentence_transformer = embeddings.SentenceTransformerWrapperEmbedding(
    #     augmentation_transform=augmentation_transforms_seed_none,
    #     batch_size=32,
    #     epochs=6,
    #     optimizer_params={'lr': 2e-2},
    # )

    # searcher_faiss = similarity_search.FaissSearch
    searcher_chroma = similarity_search.ChromaDBSearch

    pipeline = api.Pipeline(
        dataset=tmp_dataset.target.values,
        preprocessing=preprocessing_list,
        model=model_count_vectorizer_char,
        searcher=searcher_chroma,
        verbose=True,
    )
    pipeline.save('./src/models/weights', PIPELINE_NAME)
