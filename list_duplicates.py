# shows all duplicates in a list 
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# first sort the list
sorted_list = sorted(some_list)

repeated = []

for index, item in enumerate(sorted_list):
  if index and sorted_list[index - 1] == item:
    repeated.append(item)

print(repeated)

