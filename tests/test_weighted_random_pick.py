#!/usr/bin/env python3

from unittest import TestCase

from algorithms.weighted_random_pick.randpck import randpck

class TestWeightedRandomPick(TestCase):

    def test_weightedRandomPick(self):
        print("Testing Weighted Random Pick...", end="")

        # Sample 1 tests
        population = [("A", 5), ("B", 2), ("C", 3)]

        picked = randpck(population, lambda: 0)
        self.assertEqual(picked, "A")

        picked = randpck(population, lambda: 0.49999)
        self.assertEqual(picked, "A")

        picked = randpck(population, lambda: 0.50001)
        self.assertEqual(picked, "B")

        picked = randpck(population, lambda: 0.69999)
        self.assertEqual(picked, "B")

        picked = randpck(population, lambda: 0.70001)
        self.assertEqual(picked, "C")

        picked = randpck(population, lambda: 0.99999)
        self.assertEqual(picked, "C")

        # Sample 2 tests
        population = [("A", 4.21), ("B", 0), ("C", 6.329), ("D", 1)]

        picked = randpck(population, lambda: 0)
        self.assertEqual(picked, "A")

        picked = randpck(population, lambda: 0.17332)
        self.assertEqual(picked, "A")

        picked = randpck(population, lambda: 0.36484)
        self.assertEqual(picked, "A")

        picked = randpck(population, lambda: 0.36484)
        self.assertEqual(picked, "A")

        picked = randpck(population, lambda: 0.36485)
        self.assertEqual(picked, "C")

        picked = randpck(population, lambda: 0.91333)
        self.assertEqual(picked, "C")

        picked = randpck(population, lambda: 0.91334)
        self.assertEqual(picked, "D")

        picked = randpck(population, lambda: 0.95987)
        self.assertEqual(picked, "D")

        # Sample 3 tests
        population = []

        picked = randpck(population, lambda: 0.5)
        self.assertEqual(picked, None)

        print(" ok")
