"""
Author: robalar <rbthales@gmail.com>
URL: github.com/robalar/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""

#MOVE TO CONFIG
SOCKS_PORT = 7000
PROXIES = {'http': 'socks5://localhost:{0}'.format(SOCKS_PORT),
           'https': 'socks5://localhost:{0}'.format(SOCKS_PORT)}
EXCLUDE_EXIT_NODES = ['gb']
ENABLE_PROXY = True

MEDIA_DIR = './files'

DEBUG = False
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

#Move proxy stuff?
def start_tor_proxy():
    """Start the tor proxy on the preselected ports"""
    #start tor
    logger.info('Starting tor')
    logger.info('proxy: {0}'.format(PROXIES['http']))
    try:
        global TOR  # forgive me o Python gods and the mighty PEP8
        TOR = stem.process.launch_tor_with_config(config={'SocksPort':str(SOCKS_PORT), 'ExcludeExitNodes': EXCLUDE_EXIT_NODES})
    except Exception as exc:
        logger.error('Error starting tor, are you running two instances?')
        raise exc
    
    #set enviroment varibles which requests will use for all traffic
    os.environ['HTTP_PROXY'] = PROXIES.get('http')  #Fix monkey patching?
    os.environ['HTTPS_PROXY'] = PROXIES.get('https')
    
    #get ip and location info
    ip_info = json.loads(requesocks.get('http://ip-api.com/json').text)
    logger.info('IP address: {0}'.format(ip_info['query']))
    logger.info('Location: {0}'.format(ip_info['country']))

def kill_tor_proxy():
    """Kill the tor proxy"""
    logger.info('Killing tor')
    TOR.kill()
