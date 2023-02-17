import unittest
from principal import soma

class TestPrincipal(unittest.TestCase):    
    def test_soma( self):
        resultato = soma(1,2)
        self.assertEqual(resultato,3)  
    
    def test_soma2( self):
        self.assertEqual(soma(3,4),7)      

if __name__ == '__main__':
    unittest.main()        