Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> theSum = 0.0
>>> while True:
	data = input("Enter a number or just enter to quit: ")
	if data == "":
		break
	number = float(data)
	theSum += number

	
Enter a number or just enter to quit: 8
Enter a number or just enter to quit: 
>>> print("theSum is", theSum)
theSum is 8.0
>>> 
================================ RESTART: Shell ================================
>>> while True:
	number = int(input("Enter the numeric grade: "))
	if number >= 0 and number <= 100:
		break
	else:
		print("Error: Grade must be between 100 and 0")
	print(number)

	
Enter the numeric grade: 78
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print(number)
78
>>> 
================================ RESTART: Shell ================================
>>> done= False
>>> while not done:
	number = int(input("Enter the numeric grade: "))
	if number >= 0 and number <= 100:
		done = True
	else:
		print("Error: grade must be between 100 and 0")

Enter the numeric grade: 68
>>> print(number)
68
>>> 