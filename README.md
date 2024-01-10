# Django NoteApp API

## Introduction
This Django NoteApp is a simple backend application build with `Django Rest Framework`. It is designed for managing notes. Users can create, view, update, and delete notes, providing a straightforward solution for organizing information.

## Features
- **CRUD Operations:** Perform Create, Read, Update, and Delete operations on notes.
- **User Authentication:** Users can register, log in, and authenticate to manage their own notes securely.
- **RDS PostgreSQL Database:** Utilizes RDS PostgreSQL for efficient data storage and retrieval.
- **API Endpoints:** Well-defined API endpoints for interacting with the application.

## Project Structure
```
NoteApp/
│
├── NoteApp/
│   ├── __pycache__/
│   │   └── ...
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Note/
│   ├── __pycache__/
│   │   └── ...
│   ├── migrations/
│   │   └── ...
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Getting Started
1. Clone the repository:
`git clone https://github.com/your-username/noteapp.git`

2. Install dependencies:
`pip install -r requirements.txt`

3. Apply migrations:
`python manage.py migrate`

4. Run the development server:
`python manage.py runserver`
