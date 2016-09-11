#!/usr/bin/env python3

# From the book Programmation efficace (ISBN 9782340-010055)
# tryalgo.org
#
# 2.2 T9 - Text on 9 keys
#
# implementor : Pierre Faivre
# date : 2016-09-07
#
# complexity :

import sys

fr_FR = {"bonjour": 5, "page": 7, "sage": 3, "paie": 4, "sa": 8}

t9 = "22233344455566677778889999"
#     abcdefghijklmnopqrstuvwxyz


def word_to_numbers(word):
    """Returns the digits corresponding to the word on a 9 keys keypad"""
    return "".join(map(lambda l: t9[ord(l)-ord('a')], word))


def build_dictionary(words):
    """Builds the textonyms dictionary"""
    d = {}

    for word, weight in words.items():
        n = word_to_numbers(word)

        if n not in d:
            d[n] = []

        d[n].append((word, weight))

    return d


def t9_guess_word(typed_keys, dictionary):
    """Returns the most likely word given the digits"""

    if len(typed_keys) < 1:
        return None

    # Lists the matching words
    match = []
    for k, v in dictionary.items():
        if k.startswith(typed_keys):
            match.extend(v)

    # print(match)

    # Keeps only the highest rated word
    highest = (None, 0)
    for word in match:
        if word[1] > highest[1]:
            highest = (word[0], word[1])

    return highest[0]


if __name__ == "__main__":
    user_input = sys.stdin.readline().rstrip('\n')

    dictionary = build_dictionary(fr_FR)

    print(t9_guess_word(user_input, dictionary))
