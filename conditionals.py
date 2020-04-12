# works with elif block conditionals
is_old = False
is_license = False

age = int(input('Enter your age: '))
is_old = age >= 18

# 0 as a string evaluates to true so have to convert it to int()
is_license = bool(int(input('Do you have a license 0/1: ')))

# elif block
if is_old and is_license:
  print('You are good')
elif is_old or is_license:
  print('Please complete the left-over checks')
else:
  print('You can\'t drive')

# ternary in python
message = 'You are older than 18.' if age >= 18 else 'You are younger than 18.'
print(message)
