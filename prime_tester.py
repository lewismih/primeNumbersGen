# Prime numbers Tests
import unittest

from prime_numbers import prime_num

class TestIsPrime(unittest.TestCase):
    '''Test the prime_num function.'''
    def test_primes(self):
        '''Test that several primes are prime.'''
        self.assertTrue(prime_num(13) != False)
        self.assertTrue(prime_num(23) != False)
        self.assertTrue(prime_num(17) != False)
        
    def test_negative(self):
        '''Test that a negative number is not prime.'''
        self.assertFalse(prime_num(-20) == False)
        self.assertFalse(prime_num(-7) == False)
        self.assertFalse(prime_num(-100) == False)
    def test_zero(self):
        '''Test that zero is not prime.'''
        self.assertFalse(prime_num(0) == False)
    def test_one(self):
        '''Test that 1 is not prime.'''
        self.assertFalse(prime_num(1) == False)
    def test_composites(self):
        '''Test that several composites are not prime.'''
        self.assertFalse(prime_num(12) == False)
        self.assertFalse(prime_num(16) == False)
        self.assertFalse(prime_num(25) == False)

if __name__ == '__main__':
    unittest.main()def tests (self):
