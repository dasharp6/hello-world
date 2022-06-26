Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = "Alan Turing"
>>> name[0]
'A'
>>> name[3]
'n'
>>> name[len(name)]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    name[len(name)]
IndexError: string index out of range
>>> name[len(name) - 1]
'g'
>>> name[-1]
'g'
>>> name[-2]
'n'
>>> 
================================ RESTART: Shell ================================
>>> data = "Hi there!"
>>> for index in range(len(data)):
	print(index, data[index])

	
0 H
1 i
2  
3 t
4 h
5 e
6 r
7 e
8 !
>>> 
