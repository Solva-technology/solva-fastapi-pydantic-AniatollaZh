[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21297292&assignment_repo_type=AssignmentRepo)
# Техническое задание: Мини-сервис управления книгами (FastAPI + Pydantic)

## Цель
Реализовать учебный сервис на FastAPI с использованием Pydantic и pydantic-settings, демонстрирующий:
- применение `Field`, `@field_validator`, `@model_validator`;
- настройку приложения через `BaseSettings`;
- организацию кода с использованием `APIRouter`.

---

## Требования к структуре проекта

```
app/
│
├── main.py
├── config.py
├── routers/
│   ├── books.py
│   └── authors.py
└── models/
    └── fake_db.py
```

---

## Описание функционала

### 1. Настройки проекта (`config.py`)

Создать класс `Settings`.

**Поля:**
- `app_name: str` — по умолчанию `"Book API"`;
- `debug: bool` — по умолчанию `True`;
- `admin_email: EmailStr`.

**Требования:**
- добавить `model_config`;
- создать singleton-like точку получения объекта `Settings()`;

---

### 2. Модели данных
Добавьте фейковую БД
```
authors = [
    {"id": 1, "name": "Leo Tolstoy", "email": "tolstoy@example.com"},
    {"id": 2, "name": "Fyodor Dostoevsky", "email": "dostoevsky@example.com"}
]

books = [
    {"id": 1, "title": "War and Peace", "author_id": 1, "year": 1869},
    {"id": 2, "title": "Crime and Punishment", "author_id": 2, "year": 1866}
]
```

---

### 3. Роутеры

#### `routers/authors.py`
Создать роутер с префиксом `/authors`.

**Эндпоинты:**
- `GET /authors` — вернуть список авторов;
- `POST /authors` — добавить нового автора;
- `GET /authors/{author_id}` — вернуть автора по ID или 404, если не найден.

#### `routers/books.py`
Создать роутер с префиксом `/books`.

**Эндпоинты:**
- `GET /books` — вернуть список книг;
- `POST /books` — добавить книгу;
- `GET /books/{book_id}` — вернуть книгу по ID;
- при добавлении книги проверять, что `author_id` существует.

---

### 4. Готоове решение упакуйте в Docker


