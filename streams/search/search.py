import streams
from streams.search import movie
from streams import providers

import html
import urllib

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

            #try:
            provider_results = provider.do_search(term)
            #except Exception as exc:
                #print 'Cannont get results from {0}: {1}'.format(provider.name, exc)
                #raise exc
                #continue

            
            results += provider_results

        return results

    def search_to_html(self, movies):
        #create base page
        page = html.HTML()

        if movies == []:
            page.p('No results found')
            return str(page)

        #create table of results
        html_table = page.table(id='searchResults')

        html_table.thead(id='tableHead')
        header = html_table.thead.tr()

        header.th('Name')
        header.th('Length')
        header.th('Rating')

        tbody = html_table.tbody()

        for _movie in movies:
            row = tbody.tr()
            #row.td(_movie.title)
            row.td(_movie.title)
            row.td(str(_movie.length))
            row.td(_movie.age_rating)
            link = 'http://localhost:8080/player?title={0}&magnet_link={1}'.format(_movie.title, urllib.quote_plus(_movie.torrents[0].magnet_link))
            row.td().a('play', href=link)

        return str(html_table)

    def __init__(self, search_term):
        #do the search and get movies
        self.movies = self.Request(search_term)
        #get the number of movies
        self.movie_count = len(self.movies)
        #make html table
        self.html_table = self.search_to_html(self.movies)
