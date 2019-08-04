import logging
from config import Config

try:
    filename = Config()['default']['logging_dir']
except:
    filename = '/tmp/dtt.log'
logging.basicConfig(filename=filename, level=logging.DEBUG)

def logger(name):
    return logging.getLogger(name)
