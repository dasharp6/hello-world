Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def average(lyst):
	"""Returns the average of the numbers in lyst."""
	theSum = 0
	for number in lyst:
		theSum += number
		return theSum / len(lyst)

	
>>> average([1, 3, 5, 7])
0.25
>>> 