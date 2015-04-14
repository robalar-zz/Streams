def provider_list():
    pass

class GenericProvider(object):
    """docstring for GenericProvider"""
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def do_search(self, search_term):
        """To be set in the child class"""
        print 'Search not implemented in provider {0}'.format(self.name)

        