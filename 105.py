Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = “myfile.txt”
SyntaxError: invalid character '“' (U+201C)
>>> name = "myfile.txt"
>>> name[0:]
'myfile.txt'
>>> name[0:1]
'm'
>>> name[0:2]
'my'
>>> name[:len(name)]
'myfile.txt'
>>> name[-3:]
'txt'
>>> name[2:6]
'file'
>>> 
