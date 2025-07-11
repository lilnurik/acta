pip install -r requirements.txt
.env
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Swagger UI: http://127.0.0.1:8000/swagger/
ReDoc UI: http://127.0.0.1:8000/redoc/