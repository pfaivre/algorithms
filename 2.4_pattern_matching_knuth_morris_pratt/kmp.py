# From the book Programmation efficace (ISBN 9782340-010055)
# tryalgo.org
#
# 2.4 Pattern matching - Knuth-Morris-Pratt
#
# implementor : Pierre Faivre
# date : 2016-09-08
#
# complexity : O(n+m) where n and m are the length of the strings

import sys


def knuth_morris_pratt(s, t):
    """Recherche la position du motif t dans la chaîne s"""

    # First loop on the sequence
    for i in range(0, len(s)):
        # Second loop on the pattern
        for j in range(0, len(t)):
            # If we reach the and of s, it's over
            if i + j > len(s):
                return -1

            # If the current character does not match
            if t[j] != s[i + j]:
                break

            # If all the characters match, bingo !
            if j >= len(t) - 1:
                return i

    # Should not be reached so far
    return -1


if __name__ == "__main__":
    s, t = sys.stdin.readline().rstrip('\n').split(" ")

    print(knuth_morris_pratt(s, t))
