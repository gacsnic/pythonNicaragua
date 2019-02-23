sudo docker restart app-admin
sudo docker exec app-db psql -U postgres -c "drop database python_ni_app"
sudo docker exec app-db psql -U postgres -c "create database python_ni_app"
sudo docker exec app-admin python manage.py migrate
sudo docker exec app-admin python manage.py loaddata fixtures/users.json
sudo docker exec app-admin python manage.py loaddata fixtures/polls.json
sudo docker exec app-admin supervisord -n -c /etc/supervisor/supervisord.conf