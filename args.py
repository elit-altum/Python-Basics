# variable number of positional, keyword arguments can be provided to functions
# they can be accessed using *args(for arguments) and **kwargs(keyword arguments)

# *args return all provided args as a tuple
# **kwargs return all the keyword args as a dictionary

def sum_func(*args, **kwargs):
  print('Positional arguments :',args) # returns all positional arguments as a tuple
  print('Positional arguments destructured :',*args) # returns individual args in tuple, destructured

  print('Keyword arguments :',kwargs) # returns keyword arguments as a dictionary
  print('Keyword arguments as keys :',*kwargs) # returns all keys/keywords 
  # print(**kwargs) returns an error 

  # summing values
  positional_sum = sum(args) # inbuilt python fn for sum of tuples, lists etc.

  # summing the dictionary
  for value in kwargs.values():
    positional_sum += value
  
  print('The final sum is: ',positional_sum)


sum_func(1,2,3,4, n1= 20, n2 = 30)
