import libtorrent as lt
import sys
import time
from collections import deque

from streams.search import torrent
import threading

class StreamEngine(object):
    
    def __init__(self, params):
        self.lt_ses = lt.session()
        self.lt_ses.listen_on(6881, 6891)
        
        self.params = params
        self.queue = deque()
        self.stream_thread = None
        self.handle = None
    
    def add_torrent_to_queue(self, torr):

        if isinstance(torr, torrent.Torrent):
            self.queue.append(torr)
        else:
            raise TypeError('{0} was not a valid torrent'.format(torr))
    
    def remove_torrent_from_queue(self, torr):
        pass
    
    def clear_queue(self):
        self.queue = deque()
    
    def get_queue(self):
        return self.queue
    
    def start_stream(self):
        self.handle = lt.add_magnet_uri(self.lt_ses, self.queue[0].magnet_link, 
                                        self.params)
        self.handle.set_sequential_download(True)
        
        self.stream_thread = threading.Thread(target=self._stream, name='stream')
        self.stream_thread.start()

    def pause_stream(self):
        pass
    
    def stop_stream(self):
        pass
    
    def _stream(self):
        while not self.handle.has_metadata():
            print 'getting meta-data'
            time.sleep(0.1)
        
        self.handle.rename_file(0, 'test.mp4')
        
        while not self.handle.is_seed():
            s = self.handle.status()

            print 'downloading %.2f%%'%(s.progress * 100)
            sys.stdout.flush()

            time.sleep(1)
    
