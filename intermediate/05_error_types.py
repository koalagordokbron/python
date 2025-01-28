### Error types ###

# SyntaxError
# print "Hola mundo!" => Error
print('Hola mundo!')

# NameError
# print(my_variable) => Error
my_variable = 'Hola mundo!'
print(my_variable)

# IndexError
my_list = ['Python', 'JS', 'PHP', 'Java', 'C#']
# print(my_list[7]) => Error
print(my_list[3])
print(my_list[-1])

# ModuleNotFoundError
# import maths => Error
import math

# AttributeError
# print(math.PI) => Error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Pablo", "Apellido": "Morcillo", "Edad": 21, 1:"Python"}
# print(my_dict['Dirección']) => Error
print(my_dict['Nombre'])

# TypeError
# print(my_list['Nombre']) => Error
# print(my_list['0']) => Error
print(my_list[0])

# ImportError
# from math import pii => Error
from math import cos

# ValueError
# my_int = int('10 años') => Error
my_int = int('10')
print(my_int)

# ZeroDivisionError
# print(4 / 0) => Error
print(4 / 2)