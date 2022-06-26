Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> theSum = 0.0
>>> data = input("enter a number or just enter to quit: ")
enter a number or just enter to quit: 8
>>> while data != "":
	number = float(data)
	theSum += number
	data = input("Enter a number or just enter to quit: ")

Enter a number or just enter to quit: 7
Enter a number or just enter to quit: 7
Enter a number or just enter to quit: 6
Enter a number or just enter to quit: 3
Enter a number or just enter to quit: 
>>> print("The sum is", theSum)
The sum is 31.0
>>> 