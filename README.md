# Django Todo Project

A simple yet powerful Todo application built with Django REST Framework and PostgreSQL.

## Project Structure

```
/config                    # Django project settings
  /settings
    development.py        # Development configuration
  urls.py                # Main URL configuration
  asgi.py                # ASGI application
  wsgi.py                # WSGI application

/todo                     # Todo application
  models.py              # Todo model definition
  views.py               # API ViewSet
  serializers.py         # DRF serializers
  urls.py                # App URL routing
  admin.py               # Django admin configuration
  /migrations            # Database migrations

manage.py                # Django management script
requirements.txt         # Python dependencies
docker-compose.yml       # Docker container configuration
```

## Features

- ✅ Create, read, update, delete (CRUD) todos
- ✅ Mark todos as completed/pending
- ✅ Filter todos by status
- ✅ Due date tracking
- ✅ RESTful API endpoints
- ✅ Django admin interface
- ✅ PostgreSQL database
- ✅ Docker containerization

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/todos/` | List all todos |
| POST | `/api/todos/` | Create a new todo |
| GET | `/api/todos/{id}/` | Get a specific todo |
| PUT | `/api/todos/{id}/` | Update a todo |
| PATCH | `/api/todos/{id}/` | Partially update a todo |
| DELETE | `/api/todos/{id}/` | Delete a todo |
| GET | `/api/todos/completed/` | List completed todos |
| GET | `/api/todos/pending/` | List pending todos |
| PATCH | `/api/todos/{id}/toggle_completed/` | Toggle completion status |

## Setup with Docker

### 1. Build and start containers
```bash
docker-compose up --build
```

### 2. Apply database migrations
```bash
docker-compose exec web python manage.py migrate
```

### 3. Create a superuser (for Django admin)
```bash
docker-compose exec web python manage.py createsuperuser
```

### 4. Access the application
- **API**: http://localhost:8000/api/todos/
- **Admin**: http://localhost:8000/admin/

## Local Development (without Docker)

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up database
```bash
python manage.py migrate
```

### 3. Create superuser
```bash
python manage.py createsuperuser
```

### 4. Run development server
```bash
python manage.py runserver
```

## Example API Requests

### Create a todo
```bash
curl -X POST http://localhost:8000/api/todos/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
```

### List all todos
```bash
curl http://localhost:8000/api/todos/
```

### Get completed todos
```bash
curl http://localhost:8000/api/todos/completed/
```

### Mark todo as completed
```bash
curl -X PATCH http://localhost:8000/api/todos/1/toggle_completed/
```

## Environment Variables

See `.env` file for configuration:
- `DJANGO_SECRET_KEY`: Secret key for Django (change in production)
- `DEBUG`: Debug mode (set to False in production)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `POSTGRES_DB`: Database name
- `POSTGRES_USER`: Database user
- `POSTGRES_PASSWORD`: Database password
- `DATABASE_URL`: Full database connection string

## Technologies

- **Django 5.0+**: Web framework
- **Django REST Framework**: RESTful API
- **PostgreSQL 16**: Database
- **Python 3.12**: Programming language
- **Docker**: Containerization

