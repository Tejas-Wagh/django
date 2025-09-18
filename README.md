# Django + Django REST Framework Setup Guide (macOS)

This guide explains how to install Python, Django, and Django REST Framework (DRF), and how to create a project and app with migrations.

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

# 🔌 Setting up Django REST Framework (DRF)

## 1. Install Django REST Framework
```bash
python3 -m pip install djangorestframework
```

---

## 2. Update Installed Apps
In **`settings.py`**, add both your app and `rest_framework` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'app_name',
]
```

---

## 3. Create a Model
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

Run migrations after creating or updating models:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

---

## 4. Create a Serializer
Create **`serializers.py`** inside your app:

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```

This serializer converts the model to JSON (and vice versa).

---

# ✅ Summary
- Install Python and Django  
- Create a project and app  
- Run migrations and start the server  
- Add **Django REST Framework** for API development  
- Define models and serializers for JSON handling  

From here, you can create **views** (`APIView` or function-based with `@api_view`) and set up **URLs** for CRUD operations.

---
