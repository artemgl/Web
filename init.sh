sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn_wsgi.conf /etc/gunicorn.d/

sudo gunicorn -w 2 -b 0.0.0.0:8080 hello:wsgi_application & gunicorn -w 2 -b 0.0.0.0:8000 /home/box/web/etc/qa.py ask.wsgi:application
