Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> first = [10, 20, 30]
>>> second = first
>>> first
[10, 20, 30]
>>> second
[10, 20, 30]
>>> first[1] = 99
>>> first
[10, 99, 30]
>>> second
[10, 99, 30]
>>> third = []
>>> for element in first:
	third.append(elemt)

	
Traceback (most recent call last):
  File "<pyshell#10>", line 2, in <module>
    third.append(elemt)
NameError: name 'elemt' is not defined
>>> first
[10, 99, 30]
>>> third
[]
>>> for element in first:
	third.append(element)

	
>>> first
[10, 99, 30]
>>> third
[10, 99, 30]
>>> first[1] = 100
>>> first
[10, 100, 30]
>>> third
[10, 99, 30]
>>> 