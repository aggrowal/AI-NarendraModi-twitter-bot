'''
This script does not do anything but is present to avoid errors in production
'''

from os import environ
from flask import Flask

APP = Flask(__name__)
APP.run(host='0.0.0.0', port=environ.get('PORT'))
