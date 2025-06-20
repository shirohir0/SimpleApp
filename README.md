# SimpleApp 🚀

Добро пожаловать в **SimpleApp** — маленькое, но яркое 😎 приложение на базе FastAPI, которое позволяет управлять списком пользователей и их полом. Ниже пошагово описано, как запустить проект у себя локально.

## Требования

- Python 3.12+
- Опционально: виртуальное окружение

## Установка зависимостей

1. Создайте виртуальное окружение (рекомендуется):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

2. Установите зависимости из `pyproject.toml`:

```bash
pip install "fastapi>=0.115.12,<0.116.0" \
            "uvicorn[standart]>=0.34.3,<0.35.0" \
            "sqlalchemy>=2.0.41,<3.0.0"
# зависимости для разработчиков
pip install "pytest==8.4.0"
```

Также можно воспользоваться файлом `requirements`:

```bash
pip install -r requirements
```

## Настройка базы данных 🎲

Приложение ожидает файл `configs/postgres_config.py` со строкой подключения к PostgreSQL. Создайте папку `configs/` и файл `postgres_config.py`, наполнив его следующим содержимым:

```python
# configs/postgres_config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    asyncpg_URL: str = "postgresql+asyncpg://user:password@localhost:5432/simpleapp"

settings = Settings()
```

`api_v1/database/engine.py` подхватит эти настройки при создании соединения. 
Если хочется попробовать SQLite, расскомментируйте пример в `engine.py`.

После настройки базы можно проинициализировать её командой:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/database/setup
```

## Запуск приложения ⚡

Из корня проекта выполните:

```bash
uvicorn main:app --reload
```

Сервис стартует по адресу `http://127.0.0.1:8000`. Документация доступна по `http://127.0.0.1:8000/docs`.

## Кратко об API

- `/api/v1/peoples` — CRUD операции с пользователями
- `/api/v1/gender` — операции с полом
- `/api/v1/database/setup` — создание и наполнение таблиц

Приятной работы! ✨
