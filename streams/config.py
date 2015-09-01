import json
import logging
import os

import streams

logger = logging.getLogger(__name__)


def get_cfg(cfg):

    cfg_path = os.path.join(streams.DATA_DIR, cfg)

    if not os.path.isfile(cfg_path):
        logger.exception('Config file {0} doesn\'t exist!'.format(cfg_path))
        raise IOError

    return cfg_path


def read_cfg(cfg):

    try:
        with open(get_cfg(cfg), 'r') as cfg_file:
            data = json.load(cfg_file)
    except ValueError:
        logger.exception('Error in {0}!'.format(cfg))
        raise ValueError

    return data


def write_cfg(cfg, dictonary):

    cfg_data = dictonary

    with open(get_cfg(cfg), 'w') as cfg_file:
        json.dump(cfg_data, cfg_file, indent=4, skipkeys=True)


class Settings(object):

    def __init__(self, default_dict, config_file=None):

        self.default_dict = default_dict
        self.config_file = config_file

        try:
            self.config = read_cfg(config_file)
        except (IOError, ValueError):
            logger.warning('Using default config, could lead to unexpected behaviour')
            self.config = default_dict
        except:
            logger.exception('Unexpected error when reading config file!')

    def __getitem__(self, item):

        return self.config[item]

    def __setitem__(self, key, value):

        # Sets config with new value
        self.config[key] = value

        # Updates config file (if there is one) with new value
        if self.config_file:
            write_cfg(self.config_file, self.config)

    def __delitem__(self, key):

        # deletes the key from the config
        del self.config[key]

        print self.config

        # Update config file
        if self.config_file:
            write_cfg(self.config_file, self.config)
