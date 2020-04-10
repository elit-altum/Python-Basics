# works with sets
my_set = {1,2,3,4,5,5}
your_set = {4,5,6,7}

# add value to sets
my_set.add(100)

# sets don't allow duplicate characters
print(my_set)

# set methods

print(my_set.intersection(your_set))
# this is same as 
print(my_set & your_set)

print(my_set.union(your_set))
# this is same as
print(my_set | your_set)

# using sets to remove duplicates from list
my_list = [1,2,2,3,4,5,5,3]

unique_list = list(set(my_list))
print(unique_list)