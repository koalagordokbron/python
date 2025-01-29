### Regular expressions ###

import re

my_str = 'Esto es una cadena de texto para probar: expresiones regulares!'
my_other_str = "Esto es otra cadena para seguir probando: expresiones regulares..."

match = re.match("Esto es una cadena", my_str, re.I)
print(match)

# es una tupla del rango donde se encuentra el match
start, end = match.span()
print(my_str[start:end])

print(re.match("Esto es una cadena", my_str, re.I))
print(re.match("Esto es una cadena", my_other_str))

# search
# genera un objeto Match con la coincidencia
search = re.search("cadena", my_str, re.I)
print(search)

# findall
# crea una lista con todas las coincidencias
findall = re.findall("cadena", my_str, re.I)
print(findall)

# split
# devuelve una lista con los elementos separados por la coincidencia
print(re.split(":", my_str))

# sub
# sustituye los elementos y devuelve el str
print(re.sub("expresiones", "EXPRESIONES", my_str))

# patterns
pattern = r"^[A-Za-z0-9_.]+@[A-Za-z0-9_.]+\.[A-Za-z0-9_.]+$"
print(re.match(pattern, "pablomorcillocuenca@gmail.com"))