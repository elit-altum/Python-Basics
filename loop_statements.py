# works with special loop statements

# pass just sends program control to the next line
for i in [1,2,3]:
  print(i)
  pass

# continue sends program control back to loop declaration
for i in [1,2,3,4,5]:
  if i == 2:
    continue

  print(i)

# break sends program control to the first line after the loop and terminates the loop
for i in [1,2,3,4,5]:
  if i == 2:
    break
  
  print(i)