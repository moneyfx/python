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
