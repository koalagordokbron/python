### Clases ###

class MyEmptyPerson:
  pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
  def __init__(self, name, surname, alias = "Sin alias"):
    self.full_name = f"{name} {surname} {alias}"
    self.__name = name # Propiedad privada

  def get_name(self):
    return self.__name
  
  def walk(self):
    print(f"{self.full_name} está caminando")

my_person = Person("Pablo", "Morcillo")

print(f"{my_person.full_name}")
my_person.walk()

my_other_person = Person("Pablo", "Morcillo", "Koala")
print(f"{my_other_person.full_name}")
my_other_person.walk()
