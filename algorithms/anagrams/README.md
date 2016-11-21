# 2.1 Anagrams

## Definition

A word _w_ is an anagram of another word _v_ if it exists a permutation of the letters that transforms _w_ in _v_.

This implementation relies on a simple hash function that sort all the letters of a given word.
Thereby all the anagrams of a word share the same signature.

hash("limace") = hash("malice") = "aceilm"

**complexity**: between _O_(_nk_ log _k_) and _O_(_n_²_k_ log _k_)

**input**: a string  
**ouptut**: list of anagrams (e.g. `[['chien', 'chine', 'niche'], ['limace', 'malice']]`)  

## usage

```sh
$ python anagrams.py < data.in
```
