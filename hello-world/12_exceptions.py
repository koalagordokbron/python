### Excepciones ###
# else se ejecuta si no se produce una excepción
# finally se ejecuta siempre, SI O SI
# else y finally son opcionales
# puede haber varios except de varios tipos, del mismo o generales

num_1 = 5
num_2 = "1"

try:
  print(num_1 + num_2)
  print("No se ha producido un error")
except:
  print("Se ha proucido un error")
else:
  print("La ejecución continúa correctamente")
finally:
  print("La ejecución continúa")


# Excepciones por tipo
try:
  print(num_1 + num_2)
  print("No se ha producido un error")
except ValueError:
  print("Se ha proucido un error de valor")
except TypeError as e:
  print("Se ha proucido un error de tipo")
  print(e)