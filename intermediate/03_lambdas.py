### Lambdas ###
# Son funciones anónimas que se pueden usar para simplificar el código
# Se puede almacenar en una variable

sum_two_values = lambda first, second: first + second
print(sum_two_values(2, 3))

multiply_two_values = lambda first, second: first * second - 3
print(multiply_two_values(4, 5))

def sum_values(value):
  return lambda first_value, second_value: first_value + second_value + value
print(sum_values(5)(2, 4))