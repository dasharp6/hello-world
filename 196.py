Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def example(functionArg, dataArg):
	return functionArg(dataArg)

>>> example(abs, -4)
4
>>> example(math.sqrt, 2)
1.4142135623730951
>>> 
================================ RESTART: Shell ================================
>>> words = ["231", "20", "-45", "99"]
>>> map(int, words)
<map object at 0x000002879D18CFA0>
>>> words
['231', '20', '-45', '99']
>>> words = list(map(int, words))
>>> words
[231, 20, -45, 99]
>>> 
================================ RESTART: Shell ================================
>>> def changePerson(sentence):
	"""Replaces first person pronouns with second person pronouns."""
	words = sentence.split()
	replyWords = []
	for word in words:
		replyWords.append(replacements.get(word, word))
	return " ".join(replyWords)

>>> 
