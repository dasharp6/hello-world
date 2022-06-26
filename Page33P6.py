Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> radius = int(input"Enter with radius: "))
SyntaxError: invalid syntax
>>> radius = int(input("Enter with radius: "))
Enter with radius: 7
>>> area = 3.14 * radius ** 2
>>> print ("The area is", area, "square units.")
The area is 153.86 square units.
>>> radius = int(input("Enter with radius: "))
Enter with radius: 6.31
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    radius = int(input("Enter with radius: "))
ValueError: invalid literal for int() with base 10: '6.31'
>>> radius = int(input("Enter with radius: "))
Enter with radius: 14.96
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    radius = int(input("Enter with radius: "))
ValueError: invalid literal for int() with base 10: '14.96'
>>> area = 3.14 * radius ** 2
>>> 