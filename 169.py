Python 3    .9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def summation(lower, upper):
	"""Arguments: A lower bound and an upper bound Returns: the sum of the numbers from lower through upper
"""
	result = 0
	while lower <= upper:
		result += lower
		lower += 1
	return result

>>> summation(1, 4)
10
>>> summation(50, 100)
3825
>>> 
