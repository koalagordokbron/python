def numbers(a, b, c):
  num_list = [a, b, c]
  max_num = max(num_list)
  min_num = min(num_list)

  num_list.remove(max_num)
  num_list.remove(min_num)
  mid_num = num_list[0]

  return f'El mayor es {max_num}, el medio es {mid_num} el menor es {min_num}'

print(numbers(1, 2, 100))