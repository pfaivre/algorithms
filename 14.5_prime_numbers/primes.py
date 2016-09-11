#!/usr/bin/env python3

# From the book Programmation efficace (ISBN 9782340-010055)
# tryalgo.org
#
# 14.5 Prime numbers
#
# implementor : Christoph Dürr and Jill-Jênn Vie
# date : 2016-09-10
#
# complexity : O(n log log n)

import sys


def primes(n):
    """Returns all the prime numbers lower than n using the Sieve of Eratosthenes"""
    p = [True] * n
    ret = [2]

    for i in range(3, n, 2):
        if p[i]:
            ret.append(i)
            for j in range(2 * i, n, i):
                p[j] = False

    return ret


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip('\n'))

    print(primes(n))
