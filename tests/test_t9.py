#!/usr/bin/env python3

from unittest import TestCase

from algorithms.t9.t9 import build_dictionary, t9_guess_word

class TestT9(TestCase):

    def test_T9(self):
        print("Testing T9...", end="")

        fr_FR = {"bonjour": 5, "page": 7, "sage": 3, "paie": 4, "sa": 8}
        dictionary = build_dictionary(fr_FR)

        # Empty input
        w = t9_guess_word("", dictionary)
        self.assertEqual(w, None)

        # Complete input
        w = t9_guess_word("2665687", dictionary)
        self.assertEqual(w, "bonjour")

        # Incomplete input with only one candidate
        w = t9_guess_word("266", dictionary)
        self.assertEqual(w, "bonjour")

        # Incomplete input with several candidates
        w = t9_guess_word("724", dictionary)
        self.assertEqual(w, "page")

        # No candidates
        w = t9_guess_word("15896", dictionary)
        self.assertEqual(w, None)

        print(" ok")
