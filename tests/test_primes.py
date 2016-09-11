#!/usr/bin/env python3

from unittest import TestCase

from algorithms.prime_numbers.primes import primes

class TestPrimes(TestCase):

    def test_primes(self):
        print("Testing Primes...", end="")
        
        # Zero
        p = primes(0)
        self.assertEqual(p, [])

        # 10 (source: Wikipedia)
        p = primes(10)
        self.assertEqual(p, [2, 3, 5, 7])

        # 100 (source: Wikipedia)
        p = primes(100)
        self.assertEqual(p, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

        print(" ok")
