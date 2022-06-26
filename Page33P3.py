Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("Your name is", name)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print ("Your name is", name)
NameError: name 'name' is not defined
>>> name = "Pistol Pete"
>>> print ("Your name is", name)
Your name is Pistol Pete
>>> 