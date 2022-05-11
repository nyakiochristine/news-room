import unittest
from app.models import Sources


class test_source(unittest.TestCase):
    
    def setUp(self):
        self.new_source = Sources()
        
def test_instance(self):
    self.assertTrue(isinstance(self.new_source, Sources))
