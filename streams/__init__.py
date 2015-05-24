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
###

import stem.process
from stem.util import term
import os

import streams.search

FULL_PATH = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(FULL_PATH)

def start_tor_proxy():
    """Start the tor proxy on the preselected ports"""
    #start tor
    print 'Starting tor'
    print 'proxy: {0}'.format(PROXIES['http'])
    try:
        global TOR  # forgive me o Python gods and the mighty PEP8
        TOR = stem.process.launch_tor_with_config(config=
                                                  {'SocksPort':str(SOCKS_PORT)})
    except Exception as exc:
        print 'Error starting tor, are you running two instances?'
        raise exc
    #set enviroment varibles
    os.environ['HTTP_PROXY'] = PROXIES.get('http')
    os.environ['HTTPS_PROXY'] = PROXIES.get('https')

def kill_tor_proxy():
    """Kill the tor proxy"""
    TOR.kill()
