algorithms [![Build Status](https://travis-ci.org/pfaivre/algorithms.svg?branch=master)](https://travis-ci.org/pfaivre/algorithms)
==========

Personal implementations of various kinds of algorithms

Some of the subjects come from the book _Programmation efficace_ by Christoph Dürr and Jill-Jênn Vie (ISBN 9782340-010055)

## Currently implemented

|     | Name | Description |
| --- | ---- | ----------- |
| 2.1 | [Anagrams](algorithms/anagrams) | List all the anagrams on a text |
| 2.2 | [T9 - Text on 9 keys](algorithms/t9) | Guess a word typed with a 9 keys keypad, like mobile phones |
| 2.4 | [Pattern matching - Knuth-Morris-Pratt](algorithms/knuth_morris_pratt) | Search a pattern on a sequence with the Knuth-Morris-Pratt approach |
| 2.7 | [Pattern matching - Rabin-Karp](algorithms/rabin_karp) | Search a pattern on a sequence with the Rabin-Karp approach |
| 14.1 | [Greatest common divisor](algorithms/greatest_common_divisor) | Greatest common divisor between two or more numbers |
| 14.5 | [Prime numbers](algorithms/prime_numbers) | List the prime numbers |
| - | [Weighted Random Pick](algorithms/weighted_random_pick) | Randomly pick an element from an array based on its weight |
| - | [CountDiv](algorithms/count_div) | Find the number of integers divisible by K in a range |
| - | [MinAvgTwoSlice](algorithms/min_avg_two_slice) | Find the slice with the minimum average in a list of numbers |

## Running tests

Unit tests has been implemented for all algorithms.  
To run all the tests at once, simply type the following command:
```sh
$ python3 -m unittest discover
```
