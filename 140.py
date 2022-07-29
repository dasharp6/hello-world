Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> example = [1, 2, 10, 11, 12, 13]
>>> example
[1, 2, 10, 11, 12, 13]
>>> example.pop()
13
>>> example
[1, 2, 10, 11, 12]
>>> example.pop(0)
1
>>> example
[2, 10, 11, 12]
>>> 
================================ RESTART: Shell ================================
>>> aList = [34, 45, 67]
>>> target = 45
>>> if target in aList:
	print(aList.index(target))

	
1
>>> else:
	
SyntaxError: invalid syntax
>>> 
================================ RESTART: Shell ================================
>>> aList = [34, 45, 67]
>>> target = 45
>>> if target in aList:
	print(aList.index(target))
else:
	print(-1)

	
1
>>> 