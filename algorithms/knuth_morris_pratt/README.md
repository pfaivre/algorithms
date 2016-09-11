# 2.4 Pattern matching - Knuth-Morris-Pratt

## Definition

We want to find the first position of a pattern _t_ in a string _s_. Their length are respectively _m_ and _n_.

**complexity**: _O_(_n_ + _m_)

**input**: two strings, the first one is the sequence and the second one is the pattern (e.g. `lalopalalali lala`)  
**ouptut**: the position of the first character of the found pattern, or -1 if not.  

## usage

```sh
$ python kmp.py < data.in
```
