import streams.search
from streams import streamer

try:
    streams.start_tor_proxy()
    s = streams.search.do_search('star wars')
    
    s_engine = streamer.StreamEngine({'save_path': './files'})
    s_engine.add_torrent_to_queue(s[0].torrents[0])
    s_engine.start_stream()    
finally:
    streams.kill_tor_proxy()
