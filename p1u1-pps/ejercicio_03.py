num = int(input('Introduce un número: '))

print(f'La tabla de multiplicar de {num} es: ')
for i in range(1, 11100):
  print(f'{num} x {i} = {num * i}')