#MOVE TO CONFIG
SOCKS_PORT = 7000
PROXIES = {'http': 'socks5://localhost:{0}'.format(SOCKS_PORT),
           'https': 'socks5://localhost:{0}'.format(SOCKS_PORT)}

ENABLE_PROXY = True
###

import stem.process
from stem.util import term
import os

import search

FULL_PATH = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(FULL_PATH)


def print_bootstrap_lines(line):
    if "Bootstrapped " in line:
        print term.format(line, term.Color.BLUE)

def start_tor_proxy():
    #start tor
    print term.format('Starting tor', term.Color.BLUE)
    print term.format('proxy: {0}'.format(PROXIES['http']), term.Color.BLUE)
    try:
        tor_process = stem.process.launch_tor_with_config(config={'SocksPort':str(SOCKS_PORT)}, init_msg_handler=print_bootstrap_lines)
    except Exception as e:
        print 'Error starting tor, are you running two instances?'
        raise e
    #set enviroment varibles
    os.environ['HTTP_PROXY'] = PROXIES.get('http')
    os.environ['HTTPS_PROXY'] = PROXIES.get('https')
