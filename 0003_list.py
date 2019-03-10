my_list = []
my_list_2 = list()
print(my_list) # []
print(my_list_2) # []

# convert string to list(char array)
chars_list = list('hello')
print(chars_list) # ['h', 'e', 'l', 'l', 'o']

length_of_list = len(chars_list)
print(length_of_list) # 5

# convert list of chars(not int) to string
str_from_list = ''.join(chars_list)
print(str_from_list) # hello

list_of_ints = [1, 2, 3]

print(list_of_ints[::-1]) # [3, 2, 1]
print(list(reversed(list_of_ints))) # [3, 2, 1]

#reverse the list in place:
list_of_ints.reverse()
print(list_of_ints) # [3, 2, 1]

list_of_ints.append(4)
print(list_of_ints) # [3, 2, 1, 4]

print('sum of list is', sum(list_of_ints)) # sum of list is 10