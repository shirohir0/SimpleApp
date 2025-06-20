# 🚀 Simple People API — FastAPI + SQLAlchemy Project

![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-success?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Status](https://img.shields.io/badge/Production%20Ready-Yes-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🧠 Описание

**Simple People API** — это продвинутое REST API-приложение на FastAPI, позволяющее:

- 👤 создавать и получать пользователей
- 🧬 устанавливать родителей (мать и отец)
- 🚻 указывать пол (мужской/женский)
- 🔎 фильтровать и сортировать данные
- ✏️ редактировать и удалять записи

---

## 📦 Стек технологий

| Технология     | Описание                      |
|----------------|-------------------------------|
| 🐍 Python      | Язык разработки (3.11+)       |
| ⚡ FastAPI     | Web-фреймворк для REST API     |
| 🐘 PostgreSQL  | База данных                   |
| 🔄 SQLAlchemy | ORM 2.0 с async-поддержкой     |
| 🧪 Pytest      | Тестирование (готово к внедрению) |
| 🐳 Docker (по желанию) | Контейнеризация       |

---

## 🗂 Структура проекта

```

SimpleApp/
├── api\_v1/
│   ├── database/          # Подключение к БД
│   ├── models/            # SQLAlchemy модели
│   ├── routers/           # Роутеры FastAPI
│   ├── schemas/           # Pydantic-схемы
│   └── services/          # Логика и бизнес-уровень
├── main.py                # Запуск сервера
├── README.md              # Это ты сейчас читаешь ✨
└── peoples.db             # SQLite (можно PostgreSQL)

```

---

## 🔥 Фичи

✅ Получить всех пользователей  
✅ Создать нового пользователя  
✅ Назначить мать и отца  
✅ Указать пол пользователя  
✅ Удалить или изменить пользователя  
✅ Автоматически удалять записи `Parents`, если удалён `People`  
✅ Фильтрация: `age`, `name`, `gender`  
✅ 💪 Структура готова под: авторизацию, пагинацию, тестирование

---

## 🔍 Примеры API

### ▶️ Получить всех пользователей с фильтром
```

GET /api/v1/peoples/?name=иван\&min\_age=20\&gender=Мужской

````

### ➕ Создать нового пользователя
```json
POST /api/v1/peoples/
{
  "name": "Иван Иванов",
  "age": 35,
  "email": "ivan@example.com",
  "gender": "Мужской",
  "mother": "Ирина",
  "father": "Николай"
}
````

### 🔄 Обновить пользователя

```
PUT /api/v1/peoples/6
```

### ❌ Удалить пользователя

```
DELETE /api/v1/peoples/6
```

---

## 📸 Swagger UI

Доступен по адресу:

```
http://localhost:8000/docs
```

![swagger\_ui](./docs/swagger_ui_example.png) <!-- при наличии картинки -->

---

## ⚙️ Запуск проекта

1. Установи зависимости:

```bash
poetry install
# или
pip install -r requirements.txt
```

2. Запусти сервер:

```bash
uvicorn main:app --reload
```

3. (опционально) Пересоздай базу данных:

```
POST /api/v1/database/setup
```

---

## 📦 TODO / План на будущее

* [x] Разделение на `routers`, `services`, `models`
* [x] Связи: `родители`, `пол`
* [x] Удаление с каскадом
* [x] Фильтрация
* [ ] ✅ Авторизация с JWT
* [ ] ✅ Пагинация и сортировка
* [ ] 🐳 Docker + PostgreSQL
* [ ] 🔐 Ограничение доступа к API
* [ ] 🧪 Pytest-тесты и CI

---

## 📄 Лицензия

Этот проект доступен по лицензии **MIT** — используй, изменяй и развивай!

---