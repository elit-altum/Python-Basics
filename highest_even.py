# a fn to return the highest even number among a given list of elements

def highest_even(li):
  highest = -1

  for value in li:
    if not (value % 2) and value > highest:
      highest = value
  
  return highest if highest != -1 else 'All odd numbers'

print(highest_even([11,7,7,533,9,31]))