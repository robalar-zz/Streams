import streams
from streams import providers

import requesocks

class YTS(providers.GenericProvider):
    """docstring for YTS"""
    def __init__(self):
        super(YTS, self).__init__('YTS', 'https://yts.to/api/v2/list_movies.json')
    
    def do_search(self, search_term):
        
        parameters = {'query_term': search_term, 'limit': 50, 'page': 1}

        #get the data
        requests_session = requesocks.session()
        request = requests_session.get(url=('https://yts.to/api/v2/list_movies.json'), params=parameters, proxies=streams.PROXIES)

        return (movie_list, number_of movies)
