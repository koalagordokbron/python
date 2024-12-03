### Diccionarios ###
# Sintaxis parecida a JSON

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Pablo", "Apellido":"Morcillo", "Edad":21, 1:"Python"}

my_dict = {
  "Nombre":"Pablo",
  "Apellido":"Morcillo",
  "Edad":21,
  "Lenguajes": {"Python", "Swift", "Kotlin"},
  1: 1.79
}

print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedrito"
print(my_dict["Nombre"])

my_dict["Calle"] = "Callejon"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Morcillo" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = my_dict.fromkeys(("Nombre", 1))
print(my_new_dict)