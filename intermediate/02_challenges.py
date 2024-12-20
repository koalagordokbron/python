### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ":
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
def fizzbuzz():
  for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
      print('fizzbuz')
    elif i % 3 == 0:
      print('fizz')
    elif i % 5 == 0:
      print('buzz')
    else:
      print(i)

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
def is_anagram(str1, str2):
  if (str1.upper() == str2.upper()):
    return False
  return sorted(str1.upper()) == sorted(str2.upper())


"""
SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci():
  prev = 0
  next = 1

  for i in range(0, 51):
    print(prev)

    fib = prev + next
    prev = next
    next = fib

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def prime():
  def is_prime(num):
    for i in range(2, num):
      if num % i == 0:
        return False
    return True
  
  for i in range(1, 101):
    if is_prime(i):
      print(i)

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
def reverse_str(str):
  reverse = ''
  for i in range(len(str) -1, -1, -1):
    reverse += str[i]

  return reverse
print(reverse_str('hola mundo'))