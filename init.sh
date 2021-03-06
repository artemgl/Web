sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn_wsgi.conf /etc/gunicorn.d/

sudo /etc/init.d/mysql restart
sudo mysql -uroot -e "create database if not exists ask_db"
mysql -uroot -e "grant all privileges on ask_db.* to 'box'@'localhost' with grant option;"

sudo python /home/box/web/ask/manage.py makemigrations qa
sudo python /home/box/web/ask/manage.py migrate

#sudo python /home/box/web/ask/manage.py createsuperuser

sudo gunicorn --chdir /home/box/web/ask/ -b 0.0.0.0:8000 ask.wsgi:application
#sudo gunicorn --chdir /home/box/web/ask/ -b 0.0.0.0:8000 ask.wsgi:application --daemon
