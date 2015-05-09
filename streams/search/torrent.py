class Torrent(object):
    """Contains all the necessary information on a torrent
        
        Attributes:
            magnet_link (string): the magnet link associated with the torrent
            quality (string): the video/audio quality of the torrent
            
            additional information can be added through kwargs but is not 
            required ie peers, seeders, leechers
    """
    def __init__(self, magnet_link, quality, **kwargs):
        """Initializes Torrent with the required information and any additional
           information provided"""
        self.magnet_link = magnet_link
        self.quality = quality
        self.__dict__.update(kwargs)
        
    def __str__(self):
        return self.magnet_link