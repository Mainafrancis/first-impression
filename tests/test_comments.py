import unittest
from app.models import Comment

class CommentTest(unittest.TestCase):
    def SetUp(self):
        self.new_comment = Comment('Test', 'This is a test content')

    def test_instance(self):
        self.assertEquals(self.new_comment,Comment)    