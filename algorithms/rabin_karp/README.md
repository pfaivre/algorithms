# 2.7 Pattern matching - Rabin-Karp

## Definition

We want to find the first position of a pattern _t_ in a string _s_. Their length are respectively _m_ and _n_.

With the Rabin-Karp approach, instead of comparing each character, we compute a hash of _t_ and of a portion of _s_ of the same size. If it collides, we perform a character by character comparison to confirm.

To be efficient, we need a hash function that 

**complexity**: _O_(_n_ + _m_) or _O_(_nm_) on the worst case

**input**: two strings, the first one is the sequence and the second one is the pattern (e.g. `helloworld low`)  
**ouptut**: the position of the first character of the found pattern, or -1 if not.  

## usage

```sh
$ python rabinkarp.py < data.in
```
