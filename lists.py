# lists in python!

# declares a multi-data-type list
things = ['Manju', 5, True, 'Singh']

# lists can be printed as a whole
print(things)


# list slicing

# even if sliced to a single element, that single element is also returned as a list
print(things[0:1:1])

# string copying 
# directly using '=' will copy the list pointer to the variable rather than the array

# for copying the array  

new_list = things[:]

# manipulating new_list should not effect things now
new_list[0] = 'Elit'

print(new_list)
print(things)