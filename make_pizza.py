from pizza import make_pizza as mp#importing one of the 2 functions from file pizza

mp(15,'pepperoni')
# make_pizza(16,'mushroom', 'prosciutto', 'provola') you have then to change every name with wich you referred to that so this won't work

#shortening the file name
import pizza as p

p.make_pizza(16,'mushroom', 'prosciutto', 'provola') #this defines it better so that all functions have their original name
# print(pizzas) this is not defined for as is written so it won't make it seen

#asking to import every function in a module
from pizza import *

make_pizza(16,'mushroom', 'prosciutto', 'provola')
print(pizzas)

