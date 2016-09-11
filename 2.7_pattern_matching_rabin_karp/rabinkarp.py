# From the book Programmation efficace (ISBN 9782340-010055)
# tryalgo.org
#
# 2.7 Pattern matching - Rabin-Karp
#
# implementor : Pierre Faivre
# date : 2016-09-11
#
# complexity : O(n + m), O(nm) on the worst case

import sys

PRIME = 72057594037927931  # Very big number used to limit the hash value with a modulo operation
# Not too big though, it should be able to be stored in a processor registry.
# In this case, PRIME is < 2^64 so it is optimized for 64-bit architectures.

DOMAIN = 128  # 128 for ASCII strings (2^7)


def rolling_hash(s):
    """Computes the initial hash of a string"""
    m = len(s)
    h = 0

    for c in s:
        m -= 1
        h += ord(c) * (DOMAIN ** m)

    return h % PRIME


def rolling_hash_update(h, length, old_char, new_char):
    """Updates an existing hash with a new character at the end, and deletes the first one"""
    # Remove the value of the first char
    h -= ord(old_char) * (DOMAIN ** (length-1))

    # Upgrade the power of 128 of all remaining chars
    h *= DOMAIN

    # And add the new one (ord(new_char * (128 ** 0))
    h += ord(new_char)

    return h % PRIME


def rabin_karp(s, t):
    """Searches the first occurence of the pattern t in the string s"""
    ht = rolling_hash(t)
    hs = rolling_hash(s[0:len(t)])

    for i in range(0, len(s) - len(t) + 1):
        # The hashes match !
        if hs == ht:
            # Check if the strings are really equal
            if s[i:i+len(t)] == t:
                return i

        if i < len(s) - len(t):
            # Translate the window and compute the new hash
            hs = rolling_hash_update(hs, len(t), s[i], s[i + len(t)])

    return -1


if __name__ == "__main__":
    s, t = sys.stdin.readline().rstrip('\n').split(" ")

    print(rabin_karp(s, t))
