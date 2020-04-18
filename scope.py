# global scope
total = 10

def count(num):
  global total
  total += num
  return total

count(10)
print(count(5))
print(total)
