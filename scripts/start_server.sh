cd biby
source env/bin/activate
python3.9 python manage.py migrate
python3.9 python manage.py collectstatic --noinput
deactivate
sudo systemctl restart uwsgi