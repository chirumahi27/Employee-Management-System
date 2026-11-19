# Employee Management System — Complete Beginner Project

A Django project with Employee and Department management, using SQLite, Django Admin, ModelForms, and HTML templates.

## Features
- Django Admin for departments and employees
- Employee list
- Add employee
- Edit employee
- Delete employee with confirmation
- Search employees by name, email, or phone
- Filter employees by department
- Form validation and success messages
- Responsive, simple CSS
- Basic automated tests

## Requirements
- Python 3.10+
- pip

## Setup on Windows (CMD or VS Code terminal)

Open a terminal in the folder containing `manage.py`:

```bat
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py makemigrations employees
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Employee list: http://127.0.0.1:8000/employees/
- Django Admin: http://127.0.0.1:8000/admin/

## First use
1. Log in to `/admin/`.
2. Create a department (for example, IT; location Bangalore).
3. Open `/employees/` and click **Add Employee**.
4. Use Edit or Delete in the Actions column to manage records.

## Project structure
- `employee_project/`: Django project settings and root URLs
- `employees/`: models, forms, views, app URLs, admin, tests
- `employees/templates/employees/`: HTML templates
- `db.sqlite3`: created after running migrations; not included in the ZIP

## Before production
This is a learning project. Do not deploy with the included development `SECRET_KEY` or `DEBUG=True`. Use environment variables, set `DEBUG=False`, configure `ALLOWED_HOSTS`, and follow Django deployment security guidance.
