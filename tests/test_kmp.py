#!/usr/bin/env python3

from unittest import TestCase

from algorithms.knuth_morris_pratt.kmp import knuth_morris_pratt

class TestKmp(TestCase):

    def test_Kmp(self):
        print("Testing Knuth-Morris-Pratt...", end="")
        
        # Empty s, empty t
        i = knuth_morris_pratt("", "")
        self.assertEqual(i, -1)

        # Empty s
        i = knuth_morris_pratt("", "lala")
        self.assertEqual(i, -1)

        # Empty t
        i = knuth_morris_pratt("lalopalalali", "")
        self.assertEqual(i, -1)

        # Simple test 1
        i = knuth_morris_pratt("lalopalalali", "lala")
        self.assertEqual(i, 6)

        # Simple test 2
        i = knuth_morris_pratt("ABC ABCDAB ABCDABCDABDE", "ABCDABD")
        self.assertEqual(i, 15)

        # No match 1
        i = knuth_morris_pratt("ABC ABCDAB ABCDABCDABDE", "ABCDABB")
        self.assertEqual(i, -1)

        print(" ok")
