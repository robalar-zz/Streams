"""
Author: robalar <rbthales@gmail.com>
URL: github.com/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""

class Torrent(object):
    """Contains all the necessary information on a torrent

        Attributes:
            magnet_link (string): the magnet link associated with the torrent
            quality (string): the video/audio quality of the torrent
            **kwargs (dictionary): additional information i.e peers, seeds
    """
    def __init__(self, magnet_link, quality, **kwargs):
        """Initialises Torrent with the required information and any additional
           information provided"""
        self.magnet_link = magnet_link
        self.quality = quality
        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns magnet link when Torrent is cast to string"""
        return self.magnet_link
