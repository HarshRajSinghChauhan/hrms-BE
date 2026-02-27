# HRMS Lite – Backend API

## Project Overview

HRMS Lite is a lightweight Human Resource Management System backend built using Django and Django REST Framework.

This API enables an admin to:

- Manage employee records
- Track daily attendance
- Update attendance status
- Filter employees by employee ID

The system is designed to be minimal, clean, and production-ready, focusing only on essential HR operations as required in the assignment.

---

## Live Deployment

Base API URL:

https://hrms-be-zn10.onrender.com/api/

Hosted on:
Render (Web Service)

Database:
Render PostgreSQL

---

## Tech Stack

- Python 3
- Django 5
- Django REST Framework
- PostgreSQL (Production)
- SQLite (Local Development)
- Gunicorn
- django-filter
- django-cors-headers
- dj-database-url

---

## Architecture Overview

Client (React Frontend)
        |
        v
Django REST API (Render)
        |
        v
PostgreSQL Database (Render)

---

## Core Features

### 1. Employee Management

- Create employee
- View employee list
- Delete employee
- Filter by employee_id

Employee Fields:
- employee_id (unique)
- full_name
- email (unique, validated)
- department
- created_at

Server-side validations:
- Unique employee_id
- Unique email
- Valid email format
- Required fields enforced

---

### 2. Attendance Management

- Mark attendance (Present / Absent)
- View attendance records
- Update attendance status (PATCH)
- Delete attendance

Attendance Fields:
- employee (linked via employee_id)
- date
- status (Present / Absent)

Constraints:
- One attendance record per employee per date
- Attendance requires valid employee_id

---

## API Endpoints

### Employee Endpoints

GET /api/employees/  
Returns all employees.

POST /api/employees/  
Creates a new employee.

DELETE /api/employees/{id}/  
Deletes an employee by primary key.

GET /api/employees/?employee_id=EMP001  
Filters employee by employee_id.

---

### Attendance Endpoints

GET /api/attendance/  
Returns all attendance records.

POST /api/attendance/  
Creates attendance record.

PATCH /api/attendance/{id}/  
Updates attendance status.

DELETE /api/attendance/{id}/  
Deletes attendance record.

---

## Sample Requests

### Create Employee

POST /api/employees/

Request Body:
{
  "employee_id": "EMP001",
  "full_name": "John Doe",
  "email": "john@example.com",
  "department": "IT"
}

---

### Mark Attendance

POST /api/attendance/

Request Body:
{
  "employee_id": "EMP001",
  "date": "2026-02-27",
  "status": "Present"
}

---

### Update Attendance Status

PATCH /api/attendance/1/

Request Body:
{
  "status": "Absent"
}

---

## Error Handling

The API returns:

- 400 Bad Request for validation errors
- 404 Not Found for invalid resources
- 201 Created for successful creation
- 200 OK for successful retrieval
- 204 No Content for successful deletion

Examples:
- Duplicate employee_id prevented
- Duplicate attendance for same employee and date prevented
- Invalid employee_id returns validation error

---

## Filtering

Employees can be filtered by:

GET /api/employees/?employee_id=EMP001

Supports exact match filtering using django-filter.

---

## Local Setup Instructions

1. Clone the repository

git clone <repository_url>  
cd HRMS-BE

2. Create virtual environment

python -m venv venv  
venv\Scripts\activate   (Windows)

3. Install dependencies

pip install -r requirements.txt

4. Run migrations

python manage.py migrate

5. Start development server

python manage.py runserver

API will be available at:

http://127.0.0.1:8000/api/

---

## Environment Variables (Production)

The following environment variables are required:

SECRET_KEY  
DEBUG=False  
ALLOWED_HOSTS=your-render-domain.onrender.com  
DATABASE_URL=<provided by Render PostgreSQL>

---

## Deployment Notes

- Backend deployed on Render Web Service
- PostgreSQL database used in production
- Gunicorn used as WSGI server
- Migrations executed during deployment
- CORS configured to allow frontend access

Start Command used in production:

python manage.py migrate && gunicorn config.wsgi:application

---

## Limitations

- Single admin user (no authentication required)
- Payroll and leave management out of scope
- No role-based access control implemented

---

## Author

Harsh Raj Singh Chauhan