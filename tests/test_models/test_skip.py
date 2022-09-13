import unittest
class MyTestCase(unittest.TestCase):
    @unittest.skip('demo of skip')
    def test_nothing(self):
        self.fail('do nothing')
