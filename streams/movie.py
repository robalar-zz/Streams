import streams

def create_movie(title, genres, torrents, url, cover_image=None, rating=None, age_rating=None, length=None):
	return _Movie(title, genres, torrents, url, cover_image, rating, age_rating, length)

class _Movie(object):

	def gen_magnet_links(self, torrent_hash, torrent_url):
		
		trackers = str()
		for tracker in streams.TRACKERS:
			trackers += "&tr="+tracker

		link = "magnet:?xt=urn:btih:{0}&dn={1}{2}".format(
			torrent_hash, torrent_url, trackers)
		return link

	def __init__(self, title, genres, torrents, url, cover_image, rating, age_rating, length):
		self.title = title
		self.genres = genres
		self.torrents = torrents
		self.url = url
		self.cover_image = cover_image
		self.rating = rating
		self.age_rating = age_rating
		self.length = length

		for torrent in self.torrents:
			magnet_link = self.gen_magnet_links(torrent['hash'], self.url)
			torrent['magnet_link'] = magnet_link