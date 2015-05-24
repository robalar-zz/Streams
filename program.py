"""
Author: robalar <rbthales@gmail.com>
URL: github.com/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""

from streams import streamer
import streams.search


try:
    streams.start_tor_proxy()
    search = streams.search.do_search('star wars')

    stream_engine = streamer.StreamEngine({'save_path': './files'})
    stream_engine.add_torrent_to_queue(search[0].torrents[0])
    stream_engine.start_stream()
finally:
    streams.kill_tor_proxy()
