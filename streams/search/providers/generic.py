class GenericProvider(object):
    """A generic provider which must be inherited by all other providers
        
        All methods here must be overloaded for the provider to function
        properly

        Attributes:
            name (string): name of provider
            url (string): url of provider
    """
    def __init__(self, name, url):
        """Initialises provider with name and url"""
        self.name = name
        self.url = url

    def do_search(self):
        """Contains the search logic of the provider"""
        print 'Search not implemented in provider {0}'.format(self.name)
