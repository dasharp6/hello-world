Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open("integers.txt", 'r')
>>> theSum = 0
>>> for line in f:
	wordlist = line.split()
	for word in wordlist:
		number = int(word)
		theSum += number

		
>>> print("The sum is", theSum)
The sum is 123553
>>> 