Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def repToInt(repString, base = 2):
	"""Converts the repString to an int in the base and returns this int."""
	decimal = 0
	exponent - len(repString) - 1
	for digit in repString:
		decimal = decimal + in(digit) * base ** exponent
		
SyntaxError: invalid syntax
>>> def repToInt(repString, base = 2):
	"""Converts the repString to an int in the base and returns this int."""
	decimal = 0
	exponent - len(repString) - 1
	for digit in repString:
		decimal = decimal + int(digit) * base ** exponent
		exponent -= 1
	return decimal

>>> repToInt("10",10)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    repToInt("10",10)
  File "<pyshell#9>", line 4, in repToInt
    exponent - len(repString) - 1
UnboundLocalError: local variable 'exponent' referenced before assignment
>>> def repToInt(repString, base = 2):
	"""Converts the repString to an int in the base and returns this int."""
	decimal = 0
	exponent = len(repString) - 1
	for digit in repString:
		decimal = decimal + int(digit) * base ** exponent
		exponent -= 1
	return decimal

>>> repToInt("10",10)
10
>>> repToInt("10",8)
8
>>> repToInt("10",2)
2
>>> repToInt("10")
2
>>> 
