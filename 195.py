Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> abs
<built-in function abs>
>>> import math
>>> math.sqrt
<built-in function sqrt>
>>> f = abs
>>> f
<built-in function abs>
>>> f(-4)
4
>>> funcs = [abs, math.sqrt]
>>> funcs
[<built-in function abs>, <built-in function sqrt>]
>>> funcs[1](2)
1.4142135623730951
>>> 
