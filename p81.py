Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> number = int(input("Enter the numeric grade: "))
Enter the numeric grade: 80
>>> if number > 89:
	letter = 'A'
elif number > 79:
	letter = 'B'
elif number > 69:
	letter = 'C'
else:
	letter = 'F'

>>> print("The letter grade is", letter)
The letter grade is B
>>> 