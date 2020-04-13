# a sample exercise to handle 2D arrays just like in pixels

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# print() by default prints on a new line therefore we provide the 'end' argument 

for row in picture:
  for pixel in row:
    if pixel:
      print('*', end='')
    else:
      print(' ', end='') 
  print('')