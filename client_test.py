'''
Created on Feb 14, 2023

@author: uwallja
'''
import unittest
from client import getRatio

class ClentTest(unittest.TestCase):

    def test_getRatio(self):
        price_a = 114.25
        price_b = 115.595
        self.assertLess(getRatio(price_a, price_b), 0)
        
        
    def test_getRatio_priceBZero(self):
        price_a = 118.24
        price_b = 0
        self.assertIsNone(getRatio(price_a, price_b))   
         


if __name__ == "__main__":
    
    unittest.main()
