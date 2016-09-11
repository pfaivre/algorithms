#!/usr/bin/env python3

from unittest import TestCase

from algorithms.anagrams.anagrams import list_anagrams

class TestAnagrams(TestCase):

    def test_anagrams(self):
        print("Testing Anagrams...", end="")

        # Empty string
        a = list_anagrams("")
        self.assertEqual(a, [])

        # No anagrams
        a = list_anagrams("azertyuiop azergyuiop")
        self.assertEqual(a, [])

        # Twice the same word
        a = list_anagrams("azerty zertya ytreza ezaryt ezarty azerty")
        self.assertEqual(len(a[0]), 5)

        # A complete sentence
        a = list_anagrams("le chien marche vers sa niche et trouve une limace de chine nue pleine de malice qui lui fait du charme")
        self.assertEqual(len(a), 4)

        print(" ok")
