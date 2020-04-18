# works with functions in python!

# the 'def' keyword tells python about function definition
# values which fn uses are parameters and the actual values passed to fn are arguments

def hello_msg(name = 'Darth Vader', age = '21'):
  print(f'Hello {name}! You are {age}.')

# as python interprets line by line, fn call should be after fn declaration always
hello_msg('elit', 19)

print(hello_msg) # outputs memory address of fn

# arguments provided in same order as fn parameters are positional arguments
# we may also skip the order to provide something like keyword arguments

hello_msg(age = 23, name = 'Chaman') # order doesn't matter

# default argument values
hello_msg(age = 23)

# functions can also be nested
def add_values():
  def actual_add(n1, n2):
    return n1 + n2
  return actual_add

# return ends the function execution and exits the function

# we may use it to assign a function to a variable
total = add_values()
print(total(5,10))