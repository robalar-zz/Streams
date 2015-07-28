"""
Author: robalar <rbthales@gmail.com>
URL: github.com/robalar/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""
#Monkey patching the DNS requests through proxy
#from lib import socks
import socket
orginal_socket = socket.socket

def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
socket.getaddrinfo = getaddrinfo

import stem
import logging
import json
import requesocks
import os

logger = logging.getLogger(__name__)

def log_ip_info():
    #get ip and location info
    ip_info = json.loads(requesocks.get('http://ip-api.com/json').text)
    logger.info('IP address: {0}'.format(ip_info['query']))
    logger.info('Location: {0}'.format(ip_info['country']))

class TorProxy(object):
    
    SOCKS_PORT = 7000
    PROXIES = {'http': 'socks5://localhost:{0}'.format(SOCKS_PORT),
           'https': 'socks5://localhost:{0}'.format(SOCKS_PORT)}
    EXCLUDE_EXIT_NODES = '{gb}'
    
    def __init__(self):
        """Start the tor proxy on the preselected ports"""
        #start tor
        logger.info('Starting tor')
        logger.info('proxy: {0}'.format(self.PROXIES['http']))
        try:
            self.proc = stem.process.launch_tor_with_config(config={'SocksPort':str(self.SOCKS_PORT), 'ExcludeNodes': self.EXCLUDE_EXIT_NODES, 'ControlPort':'9051'})
        except Exception as exc:
            logger.error('Error starting tor, are you running two instances?')
            raise exc
        
        #set enviroment varibles which requests will use for all traffic
        os.environ['HTTP_PROXY'] = self.PROXIES.get('http')  #Fix monkey patching?
        os.environ['HTTPS_PROXY'] = self.PROXIES.get('https')
        
        log_ip_info()
    
    def kill(self):
        logger.info('Killing tor proxy')
        self.proc.kill()
   
        