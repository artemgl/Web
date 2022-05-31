sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn_wsgi.conf /etc/gunicorn.d/

sudo /etc/init.d/mysql restart
sudo mysql -uroot -e "create database if not exists ask_db"

sudo python /home/box/web/ask/manage.py makemigrations qa
sudo python /home/box/web/ask/manage.py migrate

sudo gunicorn --chdir /home/box/web/ask/ -b 0.0.0.0:8000 ask.wsgi:application
