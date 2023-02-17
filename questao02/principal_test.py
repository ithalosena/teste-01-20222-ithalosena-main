import unittest
from principal import soma_vetor

class TestPrincipal(unittest.TestCase):
    def test_soma_vetor(self):
        self.assertEqual(soma_vetor([1,2,3,4,5]),15)

if __name__ == '__main__':
    unittest.main()