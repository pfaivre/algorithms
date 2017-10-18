#!/usr/bin/env python3

from unittest import TestCase

from algorithms.count_div.count_div import count_div

class TestCountDiv(TestCase):

    def test_count_div(self):
        print("Testing CountDiv...", end="")
        
        c = count_div(6, 11, 2)
        self.assertEqual(c, 3)

        c = count_div(6, 15, 3)
        self.assertEqual(c, 4)

        c = count_div(5, 23, 4)
        self.assertEqual(c, 4)

        c = count_div(9, 10, 5)
        self.assertEqual(c, 1)

        c = count_div(63621, 63623, 13)
        self.assertEqual(c, 1)

        c = count_div(63619, 63621, 13)
        self.assertEqual(c, 0)

        c = count_div(11, 345, 17)
        self.assertEqual(c, 20)

        c = count_div(10, 10, 5)
        self.assertEqual(c, 1)

        c = count_div(10, 10, 20)
        self.assertEqual(c, 0)

        c = count_div(0, 0, 11)
        self.assertEqual(c, 1)

        c = count_div(1, 1, 11)
        self.assertEqual(c, 0)

        c = count_div(11, 14, 2)
        self.assertEqual(c, 2)

        c = count_div(2000000000, 2000000000, 2000000000)
        self.assertEqual(c, 1)

        print(" ok")
