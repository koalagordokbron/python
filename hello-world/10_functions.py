### Funciones ###

def my_function():
  print("Mi función")

my_function()

### U09_Q1 ###
def palindrome(n):
  if str(n).isnumeric():
    if str(n)[::-1] == str(n):
      print(f"{n} is palindrome")
    else:
      print(f"{n} isn't a palindrome")
  else:
    print("No es un número")
### U09_Q1 ###

def prints(*text):
  print(text)

prints("Hola", "Caracola", "merienda")