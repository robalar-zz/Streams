"""
Author: robalar <rbthales@gmail.com>
URL: github.com/robalar/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""

#MOVE TO CONFIG

MEDIA_DIR = './files'

DEBUG = True
###

import os
import logging
import stem.process
import requesocks
import json
import platform
from glob import glob

if DEBUG:
    logging_level = logging.DEBUG
else:
    logging_level = logging.INFO
    
#e.g 10:48:02 PM 27/07/2015|ERROR|test
logging.basicConfig(format='%(asctime)s|%(levelname)s|%(message)s', datefmt='%I:%M:%S %p %d/%m/%Y',level=logging_level)

logger = logging.getLogger(__name__)

DIRECTORY = os.path.dirname(__file__)
FULL_PATH = os.path.abspath(DIRECTORY)
DATA_DIR = os.path.join(FULL_PATH, 'data')

PROXIES = {}

PLATFORM = platform.system()
logger.info('Running on {0}'.format(PLATFORM))

print DIRECTORY, FULL_PATH

def get_cfg(cfg):

    cfg_path = os.path.join(DATA_DIR, cfg) 

    if not os.path.isfile(cfg_path):
        logger.warning('Config file {0} doesn\'t exist! Skipping'.format(cfg))
        return {}

    try:
        with open(cfg_path) as cfg_file:
            data = json.load(cfg_file)
    except ValueError:
        logger.warning('Error in the {0}! Skipping'.format(cfg))
        return {}

    return data

def write_cfg():
    pass


