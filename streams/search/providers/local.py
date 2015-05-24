"""
Author: robalar <rbthales@gmail.com>
URL: github.com/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""

from streams.search.providers import generic
import streams
import glob 

class local(generic.GenericProvider):

    def __init__(self):
        super(local, self).__init__('local', streams.MEDIA_DIR)
    
    def do_search(self):
        video_exts = ['*.mp4', '*.flv']
        
        file_list = []
        for ext in video_exts:
            file_list += glob.glob('{0}/{1}'.format(self.url, ext))
        
        for _file in file_list:
            pass
        
provider = local()