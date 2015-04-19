import streams
from streams import providers
from streams import movie

import requesocks
import json

class YTS(providers.GenericProvider):
    """docstring for YTS"""
    def __init__(self):
        providers.GenericProvider.__init__(self, 'YTS', 'https://yts.to/api/v2/list_movies.json')
    
    def do_search(self, search_term):
        
        parameters = {'query_term': search_term, 'limit': 50, 'page': 1}

        #get the data
        requests_session = requesocks.session()
        request = requests_session.get(url=self.url, params=parameters, proxies=streams.PROXIES)

        #parse
        movie_list = self.parse_data(request)

        return movie_list

    def create_movie_list(self, data):
        movie_list = []
        for m in data['movies']:
            if m['state'] == 'DMCA Removed':
                pass
            else:
                movie_object = movie.create_movie(title=m['title'],
                                                  genres=m['genres'],
                                                  torrents=m['torrents'],
                                                  url=m['url'],
                                                  rating=m['rating'],
                                                  age_rating=m['mpa_rating'],
                                                  length=m['runtime'])
                movie_list.append(movie_object)
        return movie_list

    def parse_data(self, raw_data):
        #read json data
        json_data = json.loads(raw_data.text)
        #see if search was sucsessful
        if json_data['status'] == 'error':
            return []
        #strip away unnescicary data and convert to list of movie objects
        return self.create_movie_list(json_data['data'])

provider = YTS()