### Listas ###

list = list()
list_2 = []

print(len(list))

list = [35, 21, 20, 20, 19, 17]

print(list)
print(len(list))

list_2 = [21, 1.79, "Pablo", "Morcillo"]

print(list_2[3])
print(list_2[-1]) # empieza por el final

age, height, name, surname = list_2

list.append("Nigga") # Lo inserta al final de la lista
print(list)

list.insert(1, "Negro") # Inserta en el índice
print(list)

list.remove("Negro") # Borra el PRIMER (si se repiten) valor que le indicamos
print(list)

list.pop() # Borra el último elemento

del list[1] # borra la variable
print(list)

list_2 = list.copy()
list.clear() # Borra la lista entera
print(list)
print(list_2)

list_2.reverse() # le da la vuelta a la lista

list_2.sort()
print(list_2)