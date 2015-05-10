class Movie(object):
    """Contains all the necessary information on a movie

        Attributes:
            title (string): the title of the movie
            torrents (list of Torrent): the torrents available for the movie
            **kwargs (dictionary): additional information i.e genres, rating           
    """
    def __init__(self, title, torrents, **kwargs):
        """Initializes Movie with the required information and any additional
           information provided"""
        self.title = title
        self.torrents = torrents
        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns title of movie when Movie is cast to a string"""
        return self.title
    
    def __iter__(self):
        """When called in a loop iterates over torrents"""
        return iter(self.torrents)
