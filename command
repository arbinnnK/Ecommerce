pip install django
django-admin startproject Arbinnn .
python manage.py runserver 

django-admin startapp products
django-admin startapp shopping
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser 
pip install mysqlclient