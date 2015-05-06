import sys

import streams
from streams.providers import yts

__all__ = ['yts']


def provider_list():

    provider_modules = [getProviderModule(name) for name in __all__]

    provider_list = [provider.provider for provider in provider_modules]

    return provider_list

def getProviderModule(name):
    name = name.lower()
    prefix = "streams.providers."
    if name in __all__ and prefix + name in sys.modules:
        return sys.modules[prefix + name]
    else:
        raise Exception("Can't find " + prefix + name + " in " + repr(sys.modules))

class GenericProvider(object):
    """docstring for GenericProvider"""
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def do_search(self, search_term):
        """To be set in the child class"""
        print 'Search not implemented in provider {0}'.format(self.name)

        