# -*- coding: utf-8 -*-
"""dash.cli: provides entry point main()."""
__version__ = "0.1.0"
config_file = '~/.dashconf'

import sys
import configparser
from os import path
from os.path import expanduser
from .argparser import ArgParser

base_url = 'https://dash.cwp.govt.nz'

def main():
    print("Executing dash version {version}.".format(version=__version__))

    config = configparser.SafeConfigParser()

    if not path.isfile(expanduser(config_file)):
        print("Config file not found, lets get configured\n")
        api_email = raw_input('CWP Email Address: ')
        api_token = raw_input('CWP API Token: ')

        config.add_section('main')
        config.set('main', 'api_email', api_email)
        config.set('main', 'api_token', api_token)
        config.set('main', 'base_url', base_url)

        with open(expanduser(config_file), 'w+b') as configfile:
            config.write(configfile)

        print("You are now configured")
        exit(0)

    config.read(expanduser(config_file))

    settings = {
        'base_url': config.get('main', 'base_url'),
        'api_email': config.get('main', 'api_email'),
        'api_token': config.get('main', 'api_token')
    }

    ArgParser(settings)
