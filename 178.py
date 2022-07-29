Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def summation(lower, upper, margin):
	"""Return the sum of the numbers from lower through upper, and outputs a trace of the arguments and return values on each call"""
	blanks = " " * margin
	print(blanks, lower, upper)
	if lower > upper:
		print(blanks, 0)
		return 0
	else:
		result = lower + summation(lower + 1, upper, margin + 4)
		print(blanks, result)
		return result

	
>>> summation(1, 4, 0)
 1 4
     2 4
         3 4
             4 4
                 5 4
                 0
             4
         7
     9
 10
10
>>> 
================================ RESTART: Shell ================================
>>> Fib(n) = 1, when n = 1 or n = 2
SyntaxError: cannot assign to function call
>>> def fib(n):
	"""Returns the nth Fibonacci number."""
	if n < 3:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

	
>>> fib(1, 2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    fib(1, 2)
TypeError: fib() takes 1 positional argument but 2 were given
>>> fib(1)
1
>>> fib(3)
2
>>> fib(7)
13
>>> 
