import unittest
from app.models import Articles

class test_articles(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles()
        
def test_instance(self):
    self.assertTrue(self.new_article, Articles)