class GenericProvider(object):
    """docstring for GenericProvider"""
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def do_search(self):
        """To be set in the child class"""
        print 'Search not implemented in provider {0}'.format(self.name)
