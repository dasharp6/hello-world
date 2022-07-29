Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from functools import reduce
>>> def add(x, y): return x + y

>>> def multiply(x, y): return x * y

>>> data = [1, 2, 3, 4]
>>> reduce(add, data)
10
>>> reduce(multiply, data)
24
>>> data = [1, 2, 3, 4]
>>> reduce(lambda x, y: x + y, data)
10
>>> reduce(lambda x, y: x * y, data)
24
>>> 
================================ RESTART: Shell ================================
>>> from functools import reduce
>>> def summation(lower, upper):
	"""Returns the sum of the numbers from lower through upper."""
	if lower > upper:
		return 0
	else:
		return reduce(lambda x, y: x * y,
			      range(lower, upper + 1))

	
>>> summation(2, 7)
5040
>>> summation(8, 2)
0
>>> 