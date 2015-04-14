import streams
from streams import providers

class YTS(providers.GenericProvider):
    """docstring for YTS"""
    def __init__(self, name, url):
        super(YTS, self).__init__(name, url)
    
    def do_search(self, term):
        print 'Seaching {0} for {1}'.format(self.name, term)
