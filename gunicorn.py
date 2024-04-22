import multiprocessing
import os

chdir = os.getcwd()
bind = "unix:/run/gunicorn-polar.sock"
workers = multiprocessing.cpu_count() * 2 + 1
wsgi_app = "prproject.wsgi:application"

accesslog = "access.log"
errorlog = "error.log"
