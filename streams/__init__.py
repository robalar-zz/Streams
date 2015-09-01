"""
Author: robalar <rbthales@gmail.com>
URL: github.com/robalar/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""

# MOVE TO CONFIG

MEDIA_DIR = './files'

DEBUG = True
###

import os
import logging
import stem.process
import requesocks
import json
import platform
import streams.proxy

if DEBUG:
    logging_level = logging.DEBUG
else:
    logging_level = logging.INFO
    
# e.g 10:48:02 PM 27/07/2015|ERROR|test
logging.basicConfig(format='%(asctime)s|%(name)s|%(levelname)s|%(message)s', datefmt='%I:%M:%S %p %d/%m/%Y',
                    level=logging_level)

logger = logging.getLogger(__name__)

DIRECTORY = os.path.dirname(__file__)
FULL_PATH = os.path.abspath(DIRECTORY)
DATA_DIR = os.path.join(FULL_PATH, 'data')

PROXIES = {}

PLATFORM = platform.system()
logger.info('Running on {0}'.format(PLATFORM))


class Main(object):
    
    RUNNING = True
    
    @classmethod
    def startup(cls):
        cls.tor = streams.proxy.TorProxy()
    
    @classmethod
    def shutdown(cls):
        cls.tor.kill()
    
    @classmethod
    def main(cls):
        while cls.RUNNING:
            import pdb; pdb.set_trace()

    @classmethod
    def close(cls):
        cls.RUNNING = False

def run():
    
    Main.startup()
    
    Main.main()

    Main.shutdown()