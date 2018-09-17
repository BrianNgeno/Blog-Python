import unittest
from app.models import Blog

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_blog = Blog(category = 'Personal_Blog')