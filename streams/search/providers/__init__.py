import sys

from streams.search.providers import yts

__all__ = ['yts']

def get_provider_list():

    provider_modules = [get_provider_module(name) for name in __all__]

    provider_list = [provider.provider for provider in provider_modules]

    return provider_list

def get_provider_module(name):
    name = name.lower()
    prefix = "streams.search.providers."
    if name in __all__ and prefix + name in sys.modules:
        return sys.modules[prefix + name]
    else:
        raise Exception("Can't find " + prefix + name + " in "
                        + repr(sys.modules))
