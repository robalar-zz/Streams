def create_torrent(peers, hash, url, date_uploaded_unix, magnet_link, 
                   seeds, size_bites, quality, date_uploaded, size):
    
    return _Torrent(peers, hash, url, date_uploaded_unix, magnet_link, 
                    seeds, size_bites, quality, date_uploaded, size)

class _Torrent(object):
    """TODO: Docstring"""
    def __init__(self, peers, hash, url, date_uploaded_unix, magnet_link, 
                 seeds, size_bites, quality, date_uploaded, size):
        
        self.peers = peers
        self.hash = hash
        self.url = url
        self.date_uploaded_unix = date_uploaded_unix
        self.magnet_link = magnet_link
        self.seeds = seeds
        self.size_bites = size_bites
        self.quality = quality
        self.date_uploaded = date_uploaded
        self.size = size