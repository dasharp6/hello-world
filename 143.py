Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> third = list(first)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    third = list(first)
NameError: name 'first' is not defined
>>> first = [20, 30, 40]
>>> second = first
>>> third = list(first)
>>> first == second
True
>>> first == third
True
>>> first is second
True
>>> first is third
False
>>> 