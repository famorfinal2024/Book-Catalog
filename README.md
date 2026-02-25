# Book Catalog API

## Description
This project is a Django REST API for managing a book catalog.  
It supports CRUD operations with versioned endpoints.

## Features
- Versioned REST API (/api/v1/books/)
- Validation rule (price cannot be negative)
- Swagger API documentation
- Automated testing
- Git version control

## Technologies Used
- Django
- Django REST Framework
- drf-spectacular
- SQLite

## How to Run
1. Install dependencies:
pip install -r requirements.txt

2. Run migrations:
python manage.py migrate

3. Start server:
python manage.py runserver

4. Open Swagger:
http://127.0.0.1:8000/api/docs/

## Authors
  - Group Members:Famor, Brent Jhon 
                  Villapaña, James Ryan 
                  Navales, Ryan Christoper 
                  Yurag, Prince Jay 

