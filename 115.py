Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sentencee = input("Enter a sentence: ")
Enter a sentence: This sentence has no long words.
>>> listOfWords = sentence.split()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    listOfWords = sentence.split()
NameError: name 'sentence' is not defined
>>> list0fWords - sentence.split()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    list0fWords - sentence.split()
NameError: name 'list0fWords' is not defined
>>> list0fWords = sentence.split()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list0fWords = sentence.split()
NameError: name 'sentence' is not defined
>>> 
======================== RESTART: Shell ========================
>>> sentence = input("Enter a sentence: ")
Enter a sentence: This sentence has no long words.
>>> list0fWords = sentence.split()
>>> print("There are", len(list0fWords), "words.")
There are 6 words.
>>> sum = 0
>>> for word in list0fWords:
	sum += len(word)

	
>>> print("The average word length is", sum / len(list0fWords))
The average word length is 4.5
>>> 
