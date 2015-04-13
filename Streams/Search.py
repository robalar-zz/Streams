import Streams
from Streams import Movie

import json
import requesocks
import sys
import math
import html

def StartSearch(searchTerm, page):

	searchObject = _Search(searchTerm, page)

	return searchObject
		


class _Search(object):

	"""An object to contain all relevent information from a request to the api.

	Attributes:
		movieCount (int): number of movies returned by the search.
		resultsPerPage (int): number of movies per page of the search.
		pageCount (int): number of pages returned by the search.
		movies (list of _movie): a parsed list of movies returned by the search.
	"""

	def Request(self, parameters):

		#setup request session
		requestsSession = requesocks.session()
		#start request session
		try:
			r = requestsSession.get(url='https://yts.to/api/v2/list_movies.json', params=parameters, proxies=Streams.proxies)
		except:
			print('Unable to connect to server!')
			sys.exit()
		return r

	def ParseData(self, rawData):
		#read json data
		jsonData = json.loads(rawData.text)
		#see if search was sucsessful
		if jsonData['status'] == 'error':
			print("Search Failed!")
			sys.exit()
		#strip away unnescicary data 
		return jsonData['data']


	def PopulateMovieList(self, data):
		for m in data['movies']:
			if m['state'] == 'DMCA Removed':
				return
			else:
				movieObject = Movie.createMovie(title=m['title'], genres=m['genres'], 
				torrents=m['torrents'], url=m['url'], rating=m['rating'], ageRating=m['mpa_rating'], length=m['runtime'])
				self.movies.append(movieObject)


	def __init__(self, searchTerm, page):
		#parameters of url
		parameters = {'query_term': searchTerm, 'limit': 50, 'page': page}
		
		#request the first page
		request = self.Request(parameters)

		#parse the raw data
		data = self.ParseData(request)
		
		#set object varibles
		self.movieCount = data['movie_count']
		self.resultsPerPage = data['limit']
		self.pageCount = int(math.ceil(self.movieCount/self.resultsPerPage) + 1)

		#create list of movies
		self.movies = []

		self.PopulateMovieList(data)

		#print(data['movies'][0])

def SearchToHTML(searchObject):
	
	#create base page
	page = html.HTML()
	#create table of results
	htmlTable = page.table(id='searchResults')

	htmlTable.thead(id='tableHead')
	header = htmlTable.thead.tr()

	header.th('Name')
	header.th('Length')
	header.th('Rating')

	tbody = htmlTable.tbody()

	for movie in searchObject.movies:
		row = tbody.tr()
		row.td(movie.title)
		row.td(str(movie.length))
		row.td(movie.ageRating)

	return str(htmlTable)
