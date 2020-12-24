import configparser


class ConfProperties(object):
    def __init__(self):
        self.__config_properties = configparser.RawConfigParser()
        self.__config_properties.read('application.properties')

    def get_secret_key(self):
        return self.__config_properties['secret']['key']

    def get_secret_url(self):
        return self.__config_properties['secret']['url']

    def get_user(self):
        return self.__config_properties['security']['user']

    def get_password(self):
        return self.__config_properties['security']['password']

    def get_claim(self):
        return self.__config_properties['security']['claim']


conf_properties = ConfProperties()
