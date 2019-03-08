a = 'string1'
b = 'string2'
c = 'string3'

# these two are the same
print(a, b, c) # string1 string2 string3
print(a, b, c, sep=' ', end='\n') # string1 string2 string3

print(a, b, c, sep='##') # string1##string2##string3

print(a, b, c, end='#####\n') # string1 string2 string3#####

print(a, b, c, sep='##', end='#####\n') # string1##string2##string3#####
