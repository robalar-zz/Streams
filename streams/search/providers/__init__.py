"""
Author: robalar <rbthales@gmail.com>
URL: github.com/Streams

This file is part of streams

Streams is free software, and is distributed under the MIT licence.
See LICENCE or opensource.org/licenses/MIT
"""

import sys

from streams.search.providers import yts


__all__ = ['yts']

def get_provider_list():
    """Get all of the providers in __all__"""
    provider_modules = [get_provider_module(name) for name in __all__]

    provider_list = [provider.provider for provider in provider_modules]

    return provider_list

def get_provider_module(name):
    """get a provider from its filename"""
    name = name.lower()
    prefix = "streams.search.providers."
    if name in __all__ and prefix + name in sys.modules:
        return sys.modules[prefix + name]
    else:
        raise Exception("Can't find " + prefix + name + " in "
                        + repr(sys.modules))
