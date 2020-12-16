import unittest
import sys
sys.path.append('/home/adrian/Documents/fizzbuzz/fizzbuzz-python/app')
from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):

    def test_when_given_5_returns_buzz(self):
        self.assertEqual('buzz', fizzbuzz(5))
        
    def test_when_given_15_returns_fizzbuzz(self):
        self.assertEqual('fizzbuzz', fizzbuzz(15))

    def test_when_given_3_returns_fizz(self):
        self.assertEqual('fizz', fizzbuzz(3))

    def test_when_given_2_returns_2(self):
        self.assertEqual(2, fizzbuzz(2))
