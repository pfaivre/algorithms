#!/usr/bin/env python3

# From the book Programmation efficace (ISBN 9782340-010055)
# tryalgo.org
#
# 2.1 Anagrammes
#
# implementor : Pierre Faivre
# date : 2016-09-05
#
# complexity : between O(nk log k) and O(n²k log k)

import sys


def list_anagrams(input_text):
    anagrams = []
    signatures = {}

    # Let's split the text to work word by word
    words = input_text.split(" ")

    for word in words:
        # Computes the signature of the word (list of sorted letters)
        signature = "".join(sorted(word))

        # If the signature is new, add it to the dictionary
        if signature not in signatures:
            signatures[signature] = []

        # If this word has not already been referenced, add it
        if word not in signatures[signature]:
            signatures[signature].append(word)

    # Finally, list the anagrams, skipping the lonely words
    for signature, words in signatures.items():
        if len(words) > 1:
            anagrams.append(words)

    return anagrams


if __name__ == "__main__":
    user_input = sys.stdin.readline().rstrip('\n')

    print(list_anagrams(user_input))
