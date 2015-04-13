import Streams
from Streams import Search
from Streams import btclient
from Streams import Webserver

import tabulate
import os

def main():
	print('Enter a movie to search for:')
	usrInput = raw_input('>> ')
	search = Search.StartSearch(usrInput, 1)

	if not search.movies:
		print('Search yeilded no results')
	else:
		table = []
		for i, movie in enumerate(search.movies, 1):

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

		btclient.main([search.movies[usrInput-1].torrents[0]['magnet_link'], '-p', 'vlc', '--http', '--debug-log', 'bt-log.txt'])
				
try:
	if __name__ == '__main__':

		#Webserver.Init()
		#main()
		s = Search.StartSearch('star wars', 1)
		print s.movies[0].torrents[0]
finally:
		if Streams.ENABLE_PROXY:
			Streams.torProcess.kill()