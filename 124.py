Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> currentDirectoryPath = os.getcwd()
>>> listofFileNames = os.listdir(currentDirectoryPath)
>>> for name in listofFileNames:
	if ".py" in name:
		print(name)

		
IncomeTaxTest.py
p78tba.py
StringTest1.py
taxform.py
>>> 