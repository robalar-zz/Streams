 #!/usr/bin/python
import streams
from streams import search
from streams import btclient
from streams import webserver

import tabulate
import os

def main():
	print('Enter a movie to search for:')
	usrInput = raw_input('>> ')
	s = search.start_search(usrInput, 1)

	if not s.movies:
		print('search yeilded no results')
	else:
		table = []
		for i, movie in enumerate(s.movies, 1):

			info = [i, movie.title, str(movie.length), movie.ageRating]

			quality = ''
			for torrent in movie.torrents:
				quality += torrent['quality'] + ' '
			info.append(quality)
			table.append(info)

		print('')
		print(tabulate.tabulate(table, headers=['No', 'Title','Length', 'Rating', 'Quality(s)']))
		print('')

		print('Select movie to stream:')

		usrInput = int(raw_input('>>'))

		btclient.main([s.movies[usrInput-1].torrents[0]['magnet_link'], '-p', 'vlc', '--http', '--debug-log', 'bt-log.txt'])
				
try:
	if __name__ == '__main__':

		webserver.Init()
		#main()
		#s = search.start_search('star wars', 1)
		#print s.movies[0].torrents[0]

		
		
finally:
		if streams.ENABLE_PROXY:
			streams.tor_process.kill()