sudo git clone https://github.com/papkakrem/stepik_web_project.git /home/box/web
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
