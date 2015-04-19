import streams
from streams import torrent

def create_movie(title, genres, torrents, url, cover_image=None, rating=None,
                 age_rating=None, length=None):
    return _Movie(title, genres, torrents, url, cover_image, rating, age_rating, length)

class _Movie(object):

    def __init__(self, title, genres, torrents, url, cover_image, rating,
                 age_rating, length):
        self.title = title
        self.genres = genres
        self.torrents = []
        self.url = url
        self.cover_image = cover_image
        self.rating = rating
        self.age_rating = age_rating
        self.length = length

        for t in torrents:
            _torrent = torrent.create_torrent(peers=t['peers'], hash=t['hash'], url=t['url'], date_uploaded_unix=t['date_uploaded_unix'], magnet_link='', seeds=t['seeds'], size_bytes=t['size_bytes'], quality=t['quality'], date_uploaded=t['date_uploaded'], size=t['size'])
            
            self.torrents.append(_torrent)

            #magnet_link = self._gen_magnet_links(t['hash'], self.url)
            #t['magnet_link'] = magnet_link
