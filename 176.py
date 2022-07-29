Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def displayRange(lower, upper):
	"""Outputs the numbers from lower through upper."""
	while lower <= upper:
		print(lower)
		lower = lower + 1

		
>>> displayRange(1, 7)
1
2
3
4
5
6
7
>>> 
================================ RESTART: Shell ================================
>>> def displayRange(lower, upper):
	"""Outputs the numbers from lower through upper."""
	if lower <= upper:
		print(lower)
		displayRange(lower + 1, upper)

		
>>> displayRange(1, 7)
1
2
3
4
5
6
7
>>> 
