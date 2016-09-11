#!/usr/bin/env python3

from unittest import TestCase

from algorithms.greatest_common_divisor.gcd import gcd_list

class TestGcd(TestCase):

    def test_gcd(self):
        print("Testing GCD...", end="")
        
        # Empty input
        g = gcd_list([])
        self.assertEqual(g, None)

        # Zeros
        g = gcd_list([0, 0])
        self.assertEqual(g, 0)

        # Ones
        g = gcd_list([1, 1])
        self.assertEqual(g, 1)

        # Two numbers
        g = gcd_list([54, 24])
        self.assertEqual(g, 6)

        # Three numbers
        g = gcd_list([36, 48, 60])
        self.assertEqual(g, 12)

        # Different order
        g = gcd_list([60, 48, 36])
        self.assertEqual(g, 12)

        print(" ok")
