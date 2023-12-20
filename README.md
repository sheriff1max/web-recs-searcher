# web-recs-searcher

Два способа запуска на выбор:
1. Docker:
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
npm run serve
```