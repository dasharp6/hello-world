Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def example(required, option1 = 2, option2 = 3):
	print(required, option1, option2)

	
>>> example(1)
1 2 3
>>> example(1, 10)
1 10 3
>>> example(1, 10, 20)
1 10 20
>>> example(1, option2 = 20)
1 2 20
>>> example(1, option2 = 20, option1 = 10)
1 10 20
>>> 
