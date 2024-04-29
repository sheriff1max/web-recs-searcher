# WEB-страница по исправлению реестровых и орфографических ошибок в пользовательском вводе

Данная WEB-страница содержит в себе визуализацию работы open-source модуля [recs-searcher](https://github.com/sheriff1max/recs-searcher)

## Возможности WEB-страницы:

1. Выбор необходимой модели, решающей конкретную задачу (предварительно можно обучить новую модель на своих данных с помощью скрипта [train.py](https://github.com/sheriff1max/web-recs-searcher/blob/main/fastapi-vue/services/backend/src/models/train.py));
2. выбор количества результатов, выводимых системой;
3. возможность выбора алгоритма для интерпретации полученных результатов;
4. ввод текстовых данных;
5. просмотр результатов, посчитанных системой.

## Запуск:

Два способа запуска на выбор:
1. Docker (запускается только backend):
```
cd fastapi-vue
docker-compose up -d --build
```

2. Local run:
> Backend:
```
cd fastapi-vue/services/backend
uvicorn src.main:app --reload --host 0.0.0.0 --port 5000
```
> Frontend:
```
cd fastapi-vue/services/frontend
npm run dev
```

## Пример работы WEB-страницы

![Main page](https://github.com/sheriff1max/web-recs-searcher/blob/main/doc/images/example.png)

![A gif of the operation of the web page.](https://github.com/sheriff1max/web-recs-searcher/blob/main/doc/gifs/demo.gif)
