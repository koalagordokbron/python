### Sets ###
# No es una estructura ordenada, utiliza un hash para acceder a los elementos
# No admite elementos repetidos

my_set = {"PHP", "React", "HTML"}
my_other_set = {} # Inicialmente, esto es un diccionario

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Pablo", "Morcillo", 21}
print(type(my_other_set))

my_other_set.add("Koala")

print("Pablo" in my_other_set)
print("Nigga" in my_other_set)

my_new_set = {"Python", "JS", "Java"}.union({"PHP", "React"})
print(my_new_set.union(my_other_set).union(my_set))

print(my_new_set.difference(my_other_set))