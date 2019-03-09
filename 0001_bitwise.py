# complement of x
# ~x  This is the same as -x - 1. 
# this is useful for looping through a list from 2 sides at the same time with 0 and -1, 1 and -2, with i and ~i
print('~0 produces:', ~0) # ~0 produces: -1
print('~1 produces:', ~1) # ~1 produces: -2
print('~(-1) produces:', ~(-1)) # ~(-1) produces: 0

# left shifting 'n' times means multiplying by 2^n
# right shifting 'n' times means dividing by 2^n

# Left shift once
print('100 << 1 produces', (100 << 1)) # 100 << 1 produces 200
# right shift once
print('100 >> 1 produces', (100 >> 1)) # 100 >> 1 produces 50

# Left shift twice
print('100 << 2 produces', (100 << 2)) # 100 << 2 produces 400
# right shift twice
print('100 >> 2 produces', (100 >> 2)) # 100 >> 2 produces 25

# Left shift three times
print('100 << 3 produces', (100 << 3)) # 100 << 3 produces 800
# right shift three times
print('100 >> 3 produces', (100 >> 3)) # 100 >> 3 produces 12

# swap two variables using XOR
a = 1
b = 7

a = a ^ b
b = b ^ a
a = a ^ b

print(a, b) # 7 1
