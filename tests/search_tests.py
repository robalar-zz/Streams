from nose.tools import assert_equals
import unittest
from types import *

import streams
from streams import search
from streams.search import torrent, movie

class SearchTest(unittest.TestCase):
    
    @classmethod
    def setup_class(cls):
        print('Running search pre-test setup')        
        streams.start_tor_proxy()
    
    @classmethod
    def teardown_class(cls):
        print('killing tor')
        streams.kill_tor_proxy()
        
    def test_get_movies(self):
        s = search.do_search('star wars')
        
        assert_equals(type(s), ListType)
        
    def test_torrent(self):
        t = torrent.Torrent('magnet:?xt=urn:sha1:YNCKHTQCWBTRNJIV4WNAE',
                            '1080p', peers=23, seeds=6)
        
        assert_equals(t.magnet_link, 
                      'magnet:?xt=urn:sha1:YNCKHTQCWBTRNJIV4WNAE')
        assert_equals(str(t), 'magnet:?xt=urn:sha1:YNCKHTQCWBTRNJIV4WNAE')
        assert_equals(t.quality, '1080p')
        assert_equals(t.peers, 23)
        assert_equals(t.seeds, 6)    
        
    def test_movie(self):
        torrent1 = torrent.Torrent('magnet:?xt=urn:sha1:YNCKHTQCWBTRNJIV4WNAE',
                                   '1080p')
        torrent2 = torrent.Torrent('magnet:?xt=urn:sha1:E52SJUQCZO5C', '720p')
        m = movie.Movie('Montage of Heck', [torrent1, torrent2],
                        genre='documentary', rating='PG-13')
        for t in m:
            assert_equals(type(t), torrent.Torrent)
        assert_equals(m.title, 'Montage of Heck')
        assert_equals(str(m), 'Montage of Heck')
        assert_equals(m.torrents[0], torrent1)
        assert_equals(m.torrents[1], torrent2)
        
        assert_equals(m.genre, 'documentary')
        assert_equals(m.rating, 'PG-13')


