a = -34
sign = '0b' if a >= 0 else '-0b'

print(bin(a))

l = []
while a != 0:
    r = a % 2
    l.append(r)
    a = int(a / 2)

#handle zero
if len(l) == 0:
    l.append(0)

#print(l[::-1])
#print(list(reversed(l)))

# reverse in place
l.reverse()

print(sign + ''.join(str(x) for x in l))
