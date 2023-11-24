echo "===create migration==="
python manage.py makemigrations
echo "===migrate==="
python manage.py migrate
echo "===runserver==="
python manage.py runserver

