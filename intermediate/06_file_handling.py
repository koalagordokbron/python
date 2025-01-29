### File handling ###

# .txt file
"""
r => lectura
r+ => lectura y escritura
w => escritura
w+ => lectura y escritura, pero crea y sobreescribe el arhcivo
"""
txt_file = open('intermediate/my_file.txt', 'r+')

# print(txt_file.read()) => Lee todo el archivo
# print(txt_file.readline()) => Lee una linea
for line in txt_file.readlines():
  print(line)

# txt_file.write('\nMe gusta Java') => escribe la linea
print(txt_file.readline())

# Es una buena practica cerrar el fichero
txt_file.close()

# Para eliminar el archivo hay que importar OS
import os
# os.remove('intermediate/my_file.txt')




# .json file
import json # para poder trabajar con json

json_file = open('intermediate/my_file.json', 'r+')
json_test = {
  "name":"Pablo",
  "surname":"Morcillo",
  "age":21,
  "languages": [
    'Python',
    'Java',
    'JS',
    'Flutter'
  ]
}

# Para escribir en el archivo .json
json.dump(json_test, json_file, indent = 2)

# leer el .json
json_dict = json.load(open('intermediate/my_file.json'))
print(json_dict)

# cerrar el .json
json_file.close()




# .csv file
import csv

csv_file = open('intermediate/my_file.csv', 'r+')
csv_writer = csv.writer(csv_file)

# escribir en el .csv
csv_writer.writerow(['name', 'surname', 'age', 'language'])
csv_writer.writerow(['Pablo', 'Morcillo', '21', 'Python'])

# leer el .csv
with open('intermediate/my_file.csv') as my_csv_file:
  for line in my_csv_file.readlines():
    print(line)

csv_file.close()



# .xlsx file
# import xlrd debe instalarse el mod



# .xml file
import xml