import unittest
from principal import fatorial

class TestPrincipal(unittest.TestCase):
    def test_fat(self):
        self.assertEqual(fatorial(5),120)

    def test_fat2(self):
        self.assertEqual(fatorial(8),40320)
    
    def test_fat3(self):
        self.assertEqual(fatorial(5),10)

    def test_fat(self):
        self.assertEqual(fatorial(1),1)

    def test_fat(self):
        self.assertEqual(fatorial(0),1)



if __name__ == '__main__':
    unittest.main()