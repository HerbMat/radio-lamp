from unittest import TestCase
from unittest import mock

from configuration.ConfProperties import ConfProperties


class TestConfProperties(TestCase):

    def test_get_secret_key(self):
        conf_properties = ConfProperties()
        with mock.patch.object(conf_properties, '_ConfProperties__config_properties') as mock_config_properties:
            mock_config_properties['secret']['key'].return_value = 'key'
            assert conf_properties.get_secret_key().return_value is 'key'

    def test_get_user(self):
        conf_properties = ConfProperties()
        with mock.patch.object(conf_properties, '_ConfProperties__config_properties') as mock_config_properties:
            mock_config_properties['secret']['user'].return_value = 'user'
            assert conf_properties.get_secret_key().return_value is 'user'

    def test_get_password(self):
        conf_properties = ConfProperties()
        with mock.patch.object(conf_properties, '_ConfProperties__config_properties') as mock_config_properties:
            mock_config_properties['secret']['password'].return_value = 'password'
            assert conf_properties.get_secret_key().return_value is 'password'
