class Movie(object):
    """Contains all the necessary information on a movie

        Attributes:
            title (string): the title of the movie
            torrents (list of Torrent): the torrents avalible for the movie

            additional information can be added through kwargs but is not
            required ie genre, cover image
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
