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

import streams.search

if DEBUG:
    logging_level = logging.DEBUG
else:
    logging_level = logging.INFO
    
#e.g 10:48:02 PM 27/07/2015|ERROR|test
logging.basicConfig(format='%(asctime)s|%(levelname)s|%(message)s', datefmt='%I:%M:%S %p %d/%m/%Y',level=logging_level)

logger = logging.getLogger(__name__)

FULL_PATH = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(FULL_PATH)

def load_config():
    pass


