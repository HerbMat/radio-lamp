from unittest import TestCase
from auth import identity, authenticate


class TestAuthHelper(TestCase):
    def test_identity_correct(self):
        payload = {"username": "admin"}
        user = identity(payload)
        assert user.username == "admin"
        assert user.password == "admin"
        assert user.id == 1

    def test_identity_not_existing_user(self):
        payload = {"username": "not_user"}
        user = identity(payload)
        assert user is None

    def test_identity_not_existing_header(self):
        payload = {"random_header": "random"}
        with self.assertRaises(KeyError) as context:
            identity(payload)
            self.assertTrue("username" in context.exception)

    def test_authenticate_success(self):
        user = authenticate("admin", "admin")
        assert user.username == "admin"
        assert user.password == "admin"
        assert user.id == 1

    def test_authenticate_bad_username(self):
        user = authenticate("badUser", "admin")
        assert user is None

    def test_authenticate_bad_password(self):
        user = authenticate("admin", "badPassword")
        assert user is None
