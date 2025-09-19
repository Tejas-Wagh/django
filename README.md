# Django + Django REST Framework Setup Guide (macOS)

This guide explains how to install Python, Django, Django REST Framework (DRF), and how to set up a project with Postgres, environment variables, and CORS.

---

## 🐍 1. Install Python on macOS

Use **Homebrew** to install the latest version of Python:

```bash
brew install python
```

✅ Verify installation:

```bash
python3 --version
pip3 --version
```

---

## 🌐 2. Install Django

Install Django using `pip`:

```bash
python3 -m pip install Django
```

✅ Verify installation:

```bash
django-admin --version
```

---

## 📂 3. Create a Django Project

Create a new project (replace `project_name` with your project’s name):

```bash
django-admin startproject project_name
```

Navigate into the project directory:

```bash
cd project_name
```

---

## 📦 4. Create an App Inside the Project

Inside your project, create an app (replace `app_name` with your app’s name):

```bash
python3 manage.py startapp app_name
```

> 🔹 Remember: Add the new `app_name` to the `INSTALLED_APPS` list in **`settings.py`**.

---

## 🛠 5. Prepare Code for Migrations

Run makemigrations to detect model changes:

```bash
python3 manage.py makemigrations
```

---

## 📑 6. Apply Migrations

Apply migrations to the database:

```bash
python3 manage.py migrate
```

---

## 🚀 7. Run Development Server

Start the Django development server:

```bash
python3 manage.py runserver
```

Default URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

# 🗄 Using PostgreSQL with Django

Django can use **Postgres locally** or via external providers like **Neon DB**.

### 1. Install Dependencies

```bash
pip install psycopg2-binary dj-database-url python-dotenv
```

### 2. Local Postgres

If running Postgres locally, create a database and user:

```bash
createdb mydb
createuser myuser --pwprompt
```

Connection string example:

```
postgresql://myuser:mypassword@localhost:5432/mydb
```

### 3. External Provider (Neon DB)

Neon will give you a connection string like:

```
postgresql://username:password@ep-xxxx.us-east-1.aws.neon.tech/neondb?sslmode=require
```

### 4. Using `.env`

Create a `.env` file in your project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://myuser:mypassword@localhost:5432/mydb
# or from Neon
# DATABASE_URL=postgresql://username:password@ep-xxxx.us-east-1.aws.neon.tech/neondb?sslmode=require
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://myfrontend.com
```

### 5. Configure `settings.py`

```python
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()  # load values from .env

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}
```

---

# 🌐 Setting up CORS

If you’re building an API to be used by a frontend (React, Vue, Next.js), you need **CORS**.

### 1. Install

```bash
pip install django-cors-headers
```

### 2. Update Installed Apps

```python
INSTALLED_APPS = [
    ...,
    "corsheaders",
    "rest_framework",
    "app_name",
]
```

### 3. Add Middleware

Make sure CORS middleware is **at the top**:

```python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...
]
```

### 4. Configure in `settings.py`

Using `.env`:

```python
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")
CORS_ALLOW_CREDENTIALS = True  # if you want cookies/sessions
```

---

# 🔌 Setting up Django REST Framework (DRF)

## 1. Install Django REST Framework

```bash
python3 -m pip install djangorestframework
```

---

## 2. Create a Model

Define your database model in **`models.py`** (inside your app):

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.name
```

Run migrations:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

---

## 3. Create a Serializer

Create **`serializers.py`** inside your app:

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```

---

# ✅ Summary

- Install Python, Django, and DRF
- Create a project and app
- Run migrations and start the server
- Use **Postgres locally** or via **Neon DB**
- Manage secrets/config with **dotenv**
- Enable **CORS** for frontend-backend communication
- Define models and serializers for JSON APIs

From here, you can create **views** and set up **URLs** for CRUD operations.
