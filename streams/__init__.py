#MOVE TO CONFIG
TRACKERS = {'udp://open.demonii.com:1337', 'udp://exodus.desync.com:6969', 
			'http://exodus.desync.com:6969/announce'}
SOCKS_PORT = 7000
PROXIES = {'http': 'socks5://localhost:{0}'.format(SOCKS_PORT), 
			'https': 'socks5://localhost:{0}'.format(SOCKS_PORT)}

ENABLE_PROXY = True
###

import stem.process
from stem.util import term
import os

FULL_PATH = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(FULL_PATH)


def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print term.format(line, term.Color.BLUE)

if ENABLE_PROXY:
	#start tor
	print(term.format('Starting tor', term.Color.BLUE))
	print(term.format('proxy: {0}'.format(PROXIES['http']), term.Color.BLUE))
	try:
		tor_process = stem.process.launch_tor_with_config(config={'SocksPort': str(SOCKS_PORT)}, init_msg_handler=print_bootstrap_lines)
	except Exception as e:
		print('Error starting tor, are you running two instances?')
		raise(e)