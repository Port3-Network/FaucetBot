import os
import logging
from logging.handlers import RotatingFileHandler

from flask import g
from flask import Flask
from flask import current_app


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('setting.py')
    if os.path.exists(os.path.join(app.root_path, 'testing.py')):
        app.debug = True
        app.config.from_pyfile('testing.py')

    configure_logging(app)

    return app

def configure_logging(app):
    app.logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '[%(asctime)s] (%(levelname)s):%(filename)s:%(funcName)s:%(lineno)d: %(message)s')

    local_log_handler = RotatingFileHandler(
        '/var/log/faucet_bot/debug.log', maxBytes=20*1024*1024, backupCount=5)
    local_log_handler.setFormatter(formatter)
    local_log_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(local_log_handler)
