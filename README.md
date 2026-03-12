# Flask Student Groups

Небольшое веб-приложение на Flask для создания группы студентов с динамическим добавлением полей формы.
Данные сохраняются в PostgreSQL в поле типа **JSONB** и могут быть получены через API.

## Возможности

* Динамическое добавление студентов в форме (jQuery)
* Сохранение данных в PostgreSQL (JSONB)
* Получение сохранённых групп через API
* Запуск через Docker

---

# Стек технологий

* Python 3.12
* Flask
* PostgreSQL
* SQLAlchemy
* jQuery
* Docker / Docker Compose

---

# Структура проекта

```
.
├── app.py
├── models.py
├── views.py
├── requirements.txt
├── Dockerfile
├── compose.yml
├── .env.example
├── templates
│   ├── base.html
│   └── form.html
└── static
    ├── css
    └── js
```

---

# Запуск проекта

### 1. Клонировать репозиторий

```
git clone https://github.com/Vorobey4K/gold09.git
cd gold09
```

---

### 2. Создать файл `.env`

Скопировать файл `.env.example` и указать свои значения переменных окружения.

```
cp .env.example .env
```

Файл `.env` должен содержать параметры подключения к базе данных PostgreSQL и секретный ключ приложения.

Пример переменных:

```
SECRET_KEY=

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=

DATABASE_URL=
```

Укажите свои значения для подключения к базе данных.

---

### 3. Запуск контейнеров

```bash
docker compose up --build
```

> Если Docker требует прав администратора, выполните команду с `sudo`.

---

### 4. Открыть приложение

Форма создания группы:

```
http://localhost:8000
```

API со списком групп:

```
http://localhost:8000/api/groups
```

---

# Как работает приложение

1. Пользователь добавляет студентов в форме.
2. jQuery динамически создаёт новые поля.
3. После отправки формы данные собираются в список.
4. Список сохраняется в PostgreSQL в поле **JSONB**.
5. API `/api/groups` возвращает сохранённые группы в формате JSON.
