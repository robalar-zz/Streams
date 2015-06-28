"""
Author: robalar <rbthales@gmail.com>
URL: github.com/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""

import streams.search
from streams import streamer


import logging

logger = logging.getLogger()

streams.start_tor_proxy()
#search = streams.search.do_search('star wars')

torrent = streams.search.torrent.Torrent('magnet:?xt=urn:btih:082FBB8F78424E47BD15674EAF73BD8F5A8B1FBC&dn=Hellboy+%282004%29+%5B720p%5D&tr=http%3A%2F%2Ftracker.yify-torrents.com%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.org%3A80&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337', '720p')

logger.info('Starting stream')
se = streamer.StreamEngine({'save_path': './files'})
se.add_torrent_to_queue(torrent)
se.start_stream()

