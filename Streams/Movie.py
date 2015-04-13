import Streams

def createMovie(title, genres, torrents, url, coverImage=None, rating=None, ageRating=None, length=None):
	return _Movie(title, genres, torrents, url, coverImage, rating, ageRating, length)

class _Movie(object):

	def genMagnetLinks(self, torrentHash, torrentUrl):
		
		trackers = str()
		for tracker in Streams.trackers:
			trackers += "&tr="+tracker

		link = "magnet:?xt=urn:btih:{0}&dn={1}{2}".format(
			torrentHash, torrentUrl, trackers)
		return link

	def __init__(self, title, genres, torrents, url,coverImage, rating, ageRating, length):
		self.title = title
		self.genres = genres
		self.torrents = torrents
		self.url = url
		self.coverImage = coverImage
		self.rating = rating
		self.ageRating = ageRating
		self.length = length

		for torrent in self.torrents:
			magnetLink = self.genMagnetLinks(torrent['hash'], self.url)
			torrent['magnet_link'] = magnetLink