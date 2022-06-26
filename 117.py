Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "Hi there!"
>>> len(s)
9
>>> s.center(11)
' Hi there! '
>>> s.count('e')
2
>>> s.count('e')
2
>>> s.endswith("there!")
True
>>> s.startswith("Hi")
True
>>> s.find("the")
3
>>> s.isalpha()
False
>>> 'abc'.isalpha()
True
>>> "326".isdigit()
True
>>> words = s.split
>>> words
<built-in method split of str object at 0x000002B7203786F0>
>>> words = s.split()
>>> words
['Hi', 'there!']
>>> " ".join(words)
'Hi there!'
>>> " ". join(words)
'Hi there!'
>>> s.upper()
'HI THERE!'
>>> s.lower()
'hi there!'
>>> s.replace('i', 'o')
'Ho there!'
>>> " Hi there! ".strip()
'Hi there!'
>>> "myfile.txt".split('.')
['myfile', 'txt']
>>> "myfile.pi".split('.')
['myfile', 'pi']
>>> "myfile.html".split('.')
['myfile', 'html']
>>> 