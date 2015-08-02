# pylint: skip-file
"""
Author: robalar <rbthales@gmail.com>
URL: github.com/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""

import streams.search
from streams import proxy
import logging

logger = logging.getLogger()

tor = proxy.TorProxy()
search = streams.search.do_search('star wars')
"""
se = streamer.StreamEngine({'save_path': './files'})
se.add_torrent_to_queue(search[0].torrents[0])
se.start_stream()"""
tor.kill()
