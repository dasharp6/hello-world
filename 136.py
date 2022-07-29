Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> x = 2
>>> [x, math.sqrt(x)]
[2, 1.4142135623730951]
>>> [x + 1]
[3]
>>> first = [1, 2, 3, 4]
>>> second = list(range(1, 5))
>>> first
[1, 2, 3, 4]
>>> second
[1, 2, 3, 4]
>>> third = list("Hi there!")
>>> third
['H', 'i', ' ', 't', 'h', 'e', 'r', 'e', '!']
>>> len(first)
4
>>> first[0]
1
>>> first[2:4]
[3, 4]
>>> first [5, 6]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    first [5, 6]
TypeError: list indices must be integers or slices, not tuple
>>> first + [5, 6]
[1, 2, 3, 4, 5, 6]
>>> first == second
True
>>> 