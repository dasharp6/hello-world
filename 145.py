Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits = ("apple", "banna")
>>> fruits
('apple', 'banna')
>>> meats = ("fish", "poultry")
>>> meats
('fish', 'poultry')
>>> food = meats + fruits
>>> food
('fish', 'poultry', 'apple', 'banna')
>>> veggies = ["celery", "beans"]
>>> tuple(veggies)
('celery', 'beans')
>>> 
=================================== RESTART: Shell ===================================
>>> badSingleton  = (3)
>>> badSingleton
3
>>> goodSingleton =(3,)
>>> goodSingleton
(3,)
>>> 