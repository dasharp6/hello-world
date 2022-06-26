Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> profit = 1000.55
>>> print('$' + profit)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print('$' + profit)
TypeError: can only concatenate str (not "float") to str
>>> print('$' + str(profit))
$1000.55
>>> 