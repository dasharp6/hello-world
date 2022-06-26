Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Width = int(input("Enter with width: "))
Enter with width: 3
>>> Length = int(input("Enter with Length: "))
Enter with Length: 10
>>> area = width * height
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    area = width * height
NameError: name 'width' is not defined
>>> area = Width * Length
>>> print("The area is", area, "square units.")
The area is 30 square units.
>>> Width = int(input("Enter with width: "))
Enter with width: 13
>>> Length = int(input("Enter with Length: "))
Enter with Length: 7
>>> area = Width * Length
>>> print("The area is", area, "square units.")
The area is 91 square units.
>>> Width = int(input("Enter with width: "))
Enter with width: 6
>>> Length = int(input("Enter with Length: "))
Enter with Length: 6
>>> area = Width * Length
>>> print("The area is", area, "square units.")
The area is 36 square units.
>>> 