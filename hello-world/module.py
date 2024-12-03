def sum_values(num_1, num_2, num_3):
  print(num_1 + num_2 + num_3)

def palindrome(n):
  if str(n).isnumeric():
    if str(n)[::-1] == str(n):
      print(f"{n} is palindrome")
    else:
      print(f"{n} isn't a palindrome")
  else:
    print("No es un número")