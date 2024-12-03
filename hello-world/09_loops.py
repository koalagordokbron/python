### Bucles ###

# While
my_condition = 0

while my_condition <= 10: 
  print(my_condition)
  my_condition += 2
else:
  print("Mi condición es mayor o igual a 10")

while my_condition < 20:
  print(my_condition)
  
  my_condition += 1
  
  if my_condition == 15:
    print("Se detiene el while")
    break
  
  print(my_condition)




# For
# Puede iterar listas, tuplas, sets y dicts (claves)
my_list = [21, 20, 21, 22, 35]

for i in my_list:
  print(i)
else:
  print("Se ha detenido el bucle for")