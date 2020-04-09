# works with strings!

name = '0123456'

# string slicing
# follows the syntax <string>[start_index:end_index:step_over]
# of the form [start_index, end_index)
print(name[3:7:2])

# string reversal
print(name[::-1])

# string methods
quote = 'to be or not to be'

# returns the string wit all letters uppercase
print(quote.upper())

# returns the string with first letter uppercase
print(quote.capitalize())

# returns the string by replacing all occurrences
print(quote.replace('be', 'me'))

# none of the methods change the actual string. quote remains same
print(quote)