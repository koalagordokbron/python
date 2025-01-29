### Package management ###

# pip
# pip list
# pip uninstall xyz
# pip show xyz
import numpy as np
import pandas
import requests

print(np.version.version)

np_array = np.array([35, 21, 365, 30, 30, 17])
print(type(np_array))

print(np_array * 2)

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics package
from mypackage import arithmetics
print(arithmetics.sum(2, 3))