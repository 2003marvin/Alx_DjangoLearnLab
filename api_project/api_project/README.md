# API Project - Django REST Framework

## Overview
This project is a RESTful API built using Django and Django REST Framework (DRF). It provides endpoints for managing books, including authentication and permission controls.

## Features
- CRUD operations for books (Create, Read, Update, Delete)
- Token-based authentication using `djangorestframework.authtoken`
- Role-based permissions for access control
- Secure API endpoints

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/api_project
```

### 2. Create and Activate Virtual Environment
```sh
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```sh
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 5. Create Superuser (Optional for Admin Access)
```sh
python manage.py createsuperuser
```

### 6. Run Development Server
```sh
python manage.py runserver
```

## Authentication Setup

### Enable Token Authentication
Ensure `rest_framework.authtoken` is added to `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'api',
]
```
Run the migration for authentication tokens:
```sh
python manage.py migrate
```

### Obtain Authentication Token
Use the following endpoint to get an authentication token:
```sh
POST http://127.0.0.1:8000/api/token/
```
Payload:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
Response:
```json
{
    "token": "your_generated_token"
}
```

Use this token in the `Authorization` header for authenticated requests:
```sh
Authorization: Token your_generated_token
```

## API Endpoints

### List All Books
```sh
GET http://127.0.0.1:8000/books_all/
```

### Retrieve a Single Book
```sh
GET http://127.0.0.1:8000/books_all/{id}/
```

### Create a New Book
```sh
POST http://127.0.0.1:8000/books_all/
```
Payload:
```json
{
    "title": "New Book",
    "author": "Author Name"
}
```

### Update a Book
```sh
PUT http://127.0.0.1:8000/books_all/{id}/
```
Payload:
```json
{
    "title": "Updated Book",
    "author": "Updated Author"
}
```

### Delete a Book
```sh
DELETE http://127.0.0.1:8000/books_all/{id}/
```

## Testing API
Use **Postman**, **cURL**, or Django's Browsable API to test endpoints.

## Deployment
For production, configure settings such as:
- `ALLOWED_HOSTS`
- `DEBUG = False`
- Database settings (PostgreSQL/MySQL)
- `DJANGO_SECRET_KEY`
- Use Gunicorn + Nginx for serving the app

## License
This project is ope