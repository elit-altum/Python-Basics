# list methods
items = [1,2,3,4]

# adds to the end of list
items.append(100)
print(items)

# adds at a particular index
items.insert(1, 44)
print(items)

# removes last item
items.pop()
print(items)

# removes an item by value
items.remove(44)
print(items)

# list unpacking
basket = [1,2,3,4,5,6,7,8,9]

a, b, *other, d, e = basket

# manipulating variables doesn't change actual value in array
a = 10

print(a)
print(other)
print(e)
print(basket)