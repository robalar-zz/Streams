"""
Author: robalar <rbthales@gmail.com>
URL: github.com/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""

#MOVE TO CONFIG
SOCKS_PORT = 7000
PROXIES = {'http': 'socks5://localhost:{0}'.format(SOCKS_PORT),
           'https': 'socks5://localhost:{0}'.format(SOCKS_PORT)}

ENABLE_PROXY = True

MEDIA_DIR = './files'

DEBUG = False
###

import os
import logging
import stem.process

import streams.search

if DEBUG:
    logging_level = logging.DEBUG
else:
    logging_level = logging.INFO

logging.basicConfig(format='%(asctime)s|%(levelname)s|%(message)s', datefmt='%I:%M:%S %p %d/%m/%Y',level=logging_level)

logger = logging.getLogger(__name__)

FULL_PATH = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(FULL_PATH)

def start_tor_proxy():
    """Start the tor proxy on the preselected ports"""
    #start tor
    logger.info('Starting tor')
    logger.info('proxy: {0}'.format(PROXIES['http']))
    try:
        global TOR  # forgive me o Python gods and the mighty PEP8
        TOR = stem.process.launch_tor_with_config(config=
                                                  {'SocksPort':str(SOCKS_PORT)})
    except Exception as exc:
        logger.error('Error starting tor, are you running two instances?')
        raise exc
    #set enviroment varibles
    os.environ['HTTP_PROXY'] = PROXIES.get('http')
    os.environ['HTTPS_PROXY'] = PROXIES.get('https')

def kill_tor_proxy():
    """Kill the tor proxy"""
    logger.info('Killing tor')
    TOR.kill()
