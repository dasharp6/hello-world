Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def summation(lower, upper):
	"""Returns the sum of the numbers from lower through upper."""
	if lower > upper:
		return 0
	else:
		return lower + summation (lower + 1, upper)

	
>>> summation(2, 5)
14
>>> 
