"""
Author: robalar <rbthales@gmail.com>
URL: github.com/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""
import requesocks
import urllib
import json

class Movie(object):
    """Contains all the necessary information on a movie.

        Attributes:
            title (string): the title of the movie
            torrents (list of Torrent): the torrents available for the movie
    """
    def __init__(self, title, torrents):
        """Initializes Movie with the required information and any additional
           information provided"""
        self.title = title
        self.torrents = torrents
        self.__dict__.update(self.get_imdb_info())

    def __str__(self):
        """Returns title of movie when Movie is cast to a string"""
        return self.title

    def __iter__(self):
        """When called in a loop iterates over torrents"""
        return iter(self.torrents)
    
    def get_imdb_info(self):
        quoted_title = urllib.quote_plus(self.title)
        request = requesocks.get('http://www.omdbapi.com/?t={0}&y=&plot=short&r=json'.format(quoted_title))
        data = json.loads(request.text)
        return data
