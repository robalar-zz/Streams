"""
Author: robalar <rbthales@gmail.com>
URL: github.com/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""

from collections import deque
import sys
import threading
import time

import libtorrent as lt
from streams.search import torrent


class StreamEngine(object):
    """Object responsible for handling the streaming of files.

       Attributes:
           lt_ses (object): the libtorrent session for streaming
           params (dict): key value pairs of parameters for the torrent
                          download (see libtorrent docs)
           queue (deque): queue of torrents to stream
           stream_thread (Thread): the tread the torrent download will be on
           handle (object): the torrent handle for the download
    """
    def __init__(self, params):
        """Sets up required variables to stream"""
        self.lt_ses = lt.session()
        self.lt_ses.listen_on(6881, 6891)

        self.params = params
        self.queue = deque()
        self.stream_thread = None
        self.handle = None

    def add_torrent_to_queue(self, torr):
        """Add a torrent to be streamed to the end of the queue"""
        if isinstance(torr, torrent.Torrent):
            self.queue.append(torr)
        else:
            raise TypeError('{0} was not a valid torrent'.format(torr))

    def remove_torrent_from_queue(self, torr):
        """Take a specified torrent out of the stream"""
        pass

    def clear_queue(self):
        """Clears the torrent queue"""
        self.queue = deque()

    def get_queue(self):
        """Returns the torrent queue"""
        return self.queue

    def start_stream(self):
        """starts a stream of the first torrent in the queue on the
            stream_thread"""
        self.handle = lt.add_magnet_uri(self.lt_ses, self.queue[0].magnet_link,
                                        self.params)
        self.handle.set_sequential_download(True)

        self.stream_thread = threading.Thread(target=self._stream,
                                              name='stream')
        self.stream_thread.start()

    def pause_stream(self):
        """NYI"""
        pass

    def stop_stream(self):
        """NYI"""
        pass

    def _stream(self):
        """Internal method to handle stream"""
        while not self.handle.has_metadata():
            print 'getting meta-data'
            time.sleep(0.1)

        self.handle.rename_file(0, 'test.mp4')

        while not self.handle.is_seed():
            stat = self.handle.status()

            print 'downloading %.2f%%'%(stat.progress * 100)
            sys.stdout.flush()

            time.sleep(1)
