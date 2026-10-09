# Django REST Framework - Status API

## Project Overview

This project is a RESTful API developed using Python, Django, and Django REST Framework to manage user status posts. Each post contains information such as title, subtitle, social media platform, description, upload time, user details, and an image.

The API uses serializers to convert Django model data into JSON responses and supports CRUD operations through HTTP methods.

## Features

- **GET:** Retrieve status posts.
- **POST:** Create a new status post.
- **PUT:** Update an existing status post.
- **DELETE:** Delete a status post.
- **Serialization:** Convert model instances into JSON-compatible data.
- **Nested Serialization:** Include related user details in status responses.
- **Media File Handling:** Store and serve uploaded images.
- **Database Integration:** Store user and status information.
- **REST API Responses:** Return structured JSON data.

## Technologies Used

- Python
- Django
- Django REST Framework
- ModelSerializer
- REST APIs
- JSON
- SQL Database
- Media File Handling

## Status Model Fields

The status data includes fields such as:

| Field | Description |
|---|---|
| `user` | Related user information |
| `title` | Status title |
| `sub_title` | Status subtitle |
| `social_media` | Social media platform |
| `description` | Status content |
| `upload_time` | Date and time of upload |
| `image` | Uploaded image URL |

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Retrieve status records |
| POST | `/` | Create a status |
| GET | `/<id>/` | Retrieve a specific status |
| PUT | `/<id>/` | Update a status |
| DELETE | `/<id>/` | Delete a status |

The exact endpoints depend on your configured Django URL patterns and views.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver
```

Open the API in your browser:

`http://127.0.0.1:8000/`

## API Testing

Test the endpoints using Postman or the Django REST Framework browsable API, if enabled.

Use JSON request bodies for creating or updating records. Configure Django media settings to serve uploaded images during local development.

## Learning Objectives

- Building REST APIs with Django REST Framework
- Implementing CRUD operations
- Using serializers and nested user data
- Handling JSON requests and responses
- Managing uploaded media files
- Working with Django models and URL routing
- Testing HTTP methods using Postman

## Future Improvements

- Add authentication and permissions.
- Add pagination and search functionality.
- Improve request validation and error handling.
- Implement consistent API responses.
- Add automated API tests.

## Disclaimer

This project is intended for learning and practice purposes.
