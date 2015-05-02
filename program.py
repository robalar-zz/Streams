#!/usr/bin/python2.7
import streams
from streams import webserver
				
try:
	if __name__ == '__main__':

		webserver.Init()

		#webserver = mp.Process(target=webserver.Init)
		#webserver.start()
		#s = search.start_search('submarine')
		#btclient.main([s.movies[0].torrents[0].magnet_link, '--http', '--debug-log', 'bt-log.txt'])

finally:
		if streams.ENABLE_PROXY:
			streams.tor_process.kill()