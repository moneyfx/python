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
for k, v in enumerate(list_of_ints):
    print('key:', k, 'value:', v)
    # key: 0 value: 1
    # key: 1 value: 2
    # key: 2 value: 3

print(list_of_ints[::-1]) # [3, 2, 1]
print(list(reversed(list_of_ints))) # [3, 2, 1]

#reverse the list in place:
list_of_ints.reverse()
print(list_of_ints) # [3, 2, 1]

list_of_ints.append(4)
print(list_of_ints) # [3, 2, 1, 4]

print('sum of list is', sum(list_of_ints)) # sum of list is 10

list_of_numbers_from_1_to_10 = [x for x in range(1, 11)]
print(list_of_numbers_from_1_to_10) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# make a set out of list
list_with_dups = [1, 5, 1, 4, 5, 2, 6]
set_from_list = set(list_with_dups)
print(set_from_list) # {1, 2, 4, 5, 6}
