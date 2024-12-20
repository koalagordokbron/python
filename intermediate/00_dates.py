### Dates ###
# Objeto datetime necesita año, mes y día de forma obligatoria, se le puede pasar hora, minutos y segundos 
# datetime agrupa todo el tiempo. time solo timepo. date solo fechas
# si los objetos del mismo tipo se puede operar con ellos
# timedelta sirve para trabajar con franjas de fechas

from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

def print_date(date):
  print(date.year)
  print(date.month)
  print(date.day)
  print(date.hour)
  print(date.minute)
  print(date.second)
  print(date.timestamp())

now = datetime.now()
print_date(now)

year_2024 = datetime(2024, 12, 20)
print_date(year_2024)

current_time = time(12, 32, 59)
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_date = date.today()
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2024, 12, 20)
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)

diff = year_2024 - now
print(diff)

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta + start_timedelta)
print(start_timedelta)