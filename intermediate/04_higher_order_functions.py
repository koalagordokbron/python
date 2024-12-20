### Higher order functions ###
# Funciones que son capaces de recibir y ejecutar funciones

def sum_one(value):
  return value + 1
def sum_five(value):
  return value + 5


def sum_two_values(first_value, second_value, f_sum):
  return f_sum(first_value + second_value)

print(sum_two_values(4, 5, sum_one))
print(sum_two_values(4, 5, sum_five))


### Closures ###
# Función que devuelve una función

def sum_ten(original_value):
  def add(value):
    return value + 10 + original_value
  return add

add_closure = sum_ten(5)
print(add_closure(10))


### Built-in Higher order functiones ###
# Funciones de orden superior de Python

numbers = [2, 5, 10, 21, 3, 30]

# Map
# Siempre va a necesitar un conjunto iterable, realiza una función sobre el conjunto iterable
print(list(map(lambda number: number * 2, numbers)))

# Filter
# Filtra según los criterios
print(list(filter(lambda num: num != 10, numbers)))

# Reduce
# Se encuentra en un módulo independiente
from functools import reduce

def sum_two_values(first_value, second_value):
  print(first_value)
  print(second_value)
  return first_value + second_value

print(reduce(sum_two_values, numbers))