#!/usr/bin/env python3

from unittest import TestCase

from algorithms.rabin_karp.rabinkarp import rabin_karp

class TestRabinKarp(TestCase):

    def test_rabinKarp(self):
        print("Testing Rabin-Karp...", end="")
        
        # Empty s, empty t
        i = rabin_karp("", "")
        self.assertEqual(i, -1)

        # Empty s
        i = rabin_karp("", "lala")
        self.assertEqual(i, -1)

        # Empty t
        i = rabin_karp("lalopalalali", "")
        self.assertEqual(i, -1)

        # Simple test 1
        i = rabin_karp("lalopalalali", "lala")
        self.assertEqual(i, 6)

        # Simple test 2
        i = rabin_karp("ABC ABCDAB ABCDABCDABDE", "ABCDABD")
        self.assertEqual(i, 15)

        # No match 1
        i = rabin_karp("ABC ABCDAB ABCDABCDABDE", "ABCDABB")
        self.assertEqual(i, -1)

        print(" ok")
