# TODO (robalar): redo search to accomidate multiple providers

import streams
from streams import movie
from streams import providers

import json
import requesocks
import sys
import math
import html

def start_search(search_term):

    search_object = _Search(search_term)

    return search_object

class _Search(object):

    """An object to contain all relevent information from a request to the api.

    Attributes:
        movie_count (int): number of movies returned by the search.
        movies (list of _Movie): a parsed list of movies returned by the 
                                 search.
        html_table (string): a HTML table of all results
    """

    def Request(self, term):

        #setup request session
        #requests_session = requesocks.session()

        results = []

        for provider in providers.provider_list():

            provider_results = []

            try:
                provider_results = provider.do_search(term)
            except Exception as exc:
                print 'Cannont get results from {0}: {1}'.format(provider.name, exc)
                continue

            
            results += provider_results

        return results

    def search_to_html(self):
        #create base page
        page = html.HTML()
        #create table of results
        html_table = page.table(id='searchResults')

        html_table.thead(id='tableHead')
        header = html_table.thead.tr()

        header.th('Name')
        header.th('Length')
        header.th('Rating')

        tbody = html_table.tbody()

        for _movie in self.movies:
            row = tbody.tr()
            row.td(_movie.title)
            row.td(str(_movie.length))
            row.td(_movie.age_rating)

        return str(html_table)

    def __init__(self, search_term):
        #parameters of url
        #parameters = {'query_term': search_term, 'limit': 50, 'page': page}
        #request the first page
        request_data = self.Request(search_term)
        #parse the raw data
        #data = self.parse_data(request)
        #set object varibles

        #self.results_per_page = data['limit']
        #self.page_count = int(math.ceil(self.movie_count/self.results_per_page)
        #                      + 1)
        #create list of movies
        self.movies = request_data
        self.movie_count = len(self.movies)
        #populate it
        #self.populate_movie_list(data)
        #print(data['movies'][0])

        #make html table
        self.search_to_html()

"""LEGACY
        #start request session
        try:
            request = requests_session.get(url=('https://yts.to/api/v2/'
                                           'list_movies.json'),
                                           params=parameters,
                                           proxies=streams.PROXIES)
        except Exception as exc:
            print 'Unable to connect to server!'
            raise exc
        return r

    # TODO (robalar): move to provider file
    def parse_data(self, raw_data):
        #read json data
        json_data = json.loads(raw_data.text)
        #see if search was sucsessful
        if json_data['status'] == 'error':
            print 'Search Failed!'
            sys.exit()
        #strip away unnescicary data
        return json_data['data']

    # TODO (robalar): move to provider file
    def populate_movie_list(self, data):
        for m in data['movies']:
            if m['state'] == 'DMCA Removed':
                return

            movie_object = movie.create_movie(title=m['title'],
                                              genres=m['genres'],
                                              torrents=m['torrents'],
                                              url=m['url'],
                                              rating=m['rating'],
                                              age_rating=m['mpa_rating'],
                                              length=m['runtime'])
            self.movies.append(movie_object)
"""
