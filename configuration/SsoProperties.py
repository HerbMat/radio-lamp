from functools import lru_cache

from configuration.ConfProperties import conf_properties, ConfProperties
import requests


class SsoProperties(object):

    def __init__(self, config_properties: ConfProperties):
        self.__confProperties = config_properties

    @lru_cache(maxsize=1)
    def get_secret_key(self):
        return requests.get(self.__confProperties.get_secret_url()).json()['secret']


sso_properties = SsoProperties(conf_properties)
