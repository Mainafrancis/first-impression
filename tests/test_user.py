import unittest
from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User('qwerty', 'qwerty@test.com', 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
            