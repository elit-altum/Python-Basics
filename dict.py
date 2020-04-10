# works with dictionaries
first_dict = {
  'a': [1,2,3],
  'b': 'elit',
  'x': 43,
  'c': True
}

print(first_dict)

# for part of a dict
print(first_dict['a'][2])

print(first_dict.pop('c'))

print(first_dict.values())

# search in dict
print('elit' in first_dict.values())

# sorted() only sorts keys of dict, not the values
print(sorted(first_dict))