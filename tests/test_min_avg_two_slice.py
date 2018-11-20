#!/usr/bin/env python3

from unittest import TestCase

from algorithms.min_avg_two_slice.min_avg_two_slice import min_avg_two_slice

class TestKmp(TestCase):

    def test_Kmp(self):
        print("Testing MinAvgTwoSlice...", end="")
        
        # Simple list
        i = min_avg_two_slice((4, 2, 2, 5, 1, 5, 8))
        self.assertEqual(i, 1)

        # All negative list
        i = min_avg_two_slice((-3, -5, -8, -4, -10))
        self.assertEqual(i, 2)

        # Mixed list
        i = min_avg_two_slice((230, -221, 2, -300, 100, -320, 8))
        self.assertEqual(i, 3)

        # Short list
        i = min_avg_two_slice((10, 0))
        self.assertEqual(i, 0)

        # All zero
        i = min_avg_two_slice((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        self.assertEqual(i, 0)

        # All -9999999
        i = min_avg_two_slice((-9999999, -9999999, -9999999, -9999999, -9999999, -9999999))
        self.assertEqual(i, 0)

        # All zero except last one being lower
        i = min_avg_two_slice((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1))
        self.assertEqual(i, 13)

        print(" ok")
