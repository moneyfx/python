empty_set = set()
print(empty_set) # set()
print(type(empty_set)) # <class 'set'>

set_with_values = {1, 2, 3}
print(set_with_values) # {1, 2, 3}
print(type(set_with_values)) # <class 'set'>

set_with_values_2 = set()
set_with_values_2.add(1)
set_with_values_2.add(2)
set_with_values_2.add(3)

print(set_with_values_2) # {1, 2, 3}
print(type(set_with_values_2)) # <class 'set'>

# this is dictionary not set
not_empty_set = {}
print(not_empty_set) # {}
print(type(not_empty_set)) # <class 'dict'>