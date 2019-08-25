import multiprocessing
import os


name = 'admin'

logfile = './logs/{}.log'.format(name)
loglevel = 'info'
logconfig = None

bind = '0.0.0.0:8000'

worker_class = 'gevent'
workers = multiprocessing.cpu_count() * 2 + 1
worker_connections = 1024
backlog = 2048
max_requests = 5120
timeout = 120
keepalive = 2

debug = os.environ.get('DEBUG', 'false') == 'true'
reload = debug
preload_app = False
daemon = False

secure_scheme_headers = {
    'X-FORWARDED-PROTOCOL': 'ssl',
    'X-FORWARDED-PROTO':    'https',
    'X-FORWARDED-SSL':      'on',
}
