Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> number = int(input("Enter the numeric grade: "))
Enter the numeric grade: 79
>>> if number > 100:
	print("Error: grade must be between 100 and 0")
elif number < 0:
	print("Error: grade must be between 100 and 0")
else:
	print("Grade is: ", input)

Grade is:  <built-in function input>
>>> print("Grade is: ", number)
Grade is:  79
>>> 
>>> number = int(input("Enter the numeric grade: "))
Enter the numeric grade: 56
>>> if number > 100 or number < 0:
	print("Error: grade must be between 100 and 0")
else:
	print("Grade is: ", number)

	
Grade is:  56
>>> 
>>> number = int(input("Enter the numeric grade: "))
Enter the numeric grade: 78
>>> if number >= 0 and number <= 100:
	print("Grade is: ", number)
else:
	print("Error grade muist be between 100 and 0")

	
Grade is:  78
>>> 