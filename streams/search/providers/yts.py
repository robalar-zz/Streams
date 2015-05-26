"""
Author: robalar <rbthales@gmail.com>
URL: github.com/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""

#TODO (robalar): clean up YTS provider
import json

import requesocks

from streams.search import movie, torrent
from streams.search.providers import generic
import math


class YTS(generic.GenericProvider):
    """Provider module for YTS"""

    trackers = {'udp://open.demonii.com:1337', 'udp://exodus.desync.com:6969',
                'http://exodus.desync.com:6969/announce'}

    def __init__(self):
        """Initialises the provider with the YTS url"""
        super(YTS, self).__init__('YTS', 
                                  'https://yts.to/api/v2/list_movies.json')

    def do_search(self, search_term):
        """Gets all pages of data from YTS"""
        limit = 50
        parameters = {'query_term': search_term, 'limit': limit, 'page': 1}

        #get the data
        requests_session = requesocks.session()
        request = requests_session.get(url=self.url, params=parameters)

        data = json.loads(request.text)
        if data['status'] == 'error':
            return []
        data = data['data']
        
        current_page = data['page_number']
        movie_count = data['movie_count']
        page_count = math.ceil(float(movie_count)/float(limit))
        
        movie_list = self.create_movie_list(data)
        
        while current_page < page_count:
            parameters['page'] += 1
            request = requests_session.get(url=self.url, params=parameters)
            _data = json.loads(request.text)
            _data = _data['data']
            current_page = _data['page_number']
            movie_list += self.create_movie_list(_data)
        
        #convert list to Torrent object
        for _movie in movie_list:
            _movie.torrents[:] = [torrent.Torrent(**_torrent) for _torrent in _movie.torrents]

        return movie_list

    def create_movie_list(self, data):
        movie_list = []
        for m in data['movies']:
            if m['state'] == 'DMCA Removed':
                pass
            else:                
                movie_object = movie.Movie(title=m['title'], genres=m['genres'],
                                           torrents=self.add_magnet_links(m['torrents']),
                                           url=m['url'],
                                           rating=m['rating'],
                                           age_rating=m['mpa_rating'],
                                           length=m['runtime'])
                movie_list.append(movie_object)
        return movie_list

    def _gen_magnet_links(self, torrent_hash, torrent_url):
        trackers = str()
        for tracker in self.trackers:
            trackers += "&tr="+tracker

        link = "magnet:?xt=urn:btih:{0}&dn={1}{2}".format(torrent_hash, 
                                                          torrent_url, trackers)
        return link
    
    def add_magnet_links(self, torrents):
        for _torrent in torrents:
            _torrent['magnet_link'] = self._gen_magnet_links(_torrent['hash'], _torrent['url'])
                
        return torrents

provider = YTS()

