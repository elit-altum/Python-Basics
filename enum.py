# works with the enumerate fn.
# enumerate returns the index + iterator for an iterable

for index, value in enumerate('Elit Altum'):
  print(index, value)

my_list = ['oranges', 'potatoes', 'apples']

for grocery in enumerate(my_list):
  print(grocery)

my_set = {1,2,3,4}

# enumerate can be used for indexing while displaying sets

for index, item in enumerate(my_set):
  print(index, item)

# using range for a list of number
numbers = list(range(2, 100))

for index, number in enumerate(numbers):
  if number == 50:
    print(index)


