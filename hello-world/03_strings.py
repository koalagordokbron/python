### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro string'
new_line_string = "Este es un string\ncon salto de linea"
name, surname, age = "Pablo", "Morcillo", 21

print(my_string + " " + my_other_string)
print(new_line_string)

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

print(f"Mi nombre es {name} {surname} y mi edad es {age}")


# División
language = "Python"
language_slice = language[0:6:2]
reverse_language = language[::-1]

print(reverse_language)
print(language_slice)



# Funciones
print(language.upper())
print(language.startswith("Py"))
print("1".isnumeric())