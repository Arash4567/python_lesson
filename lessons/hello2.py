#2-DARS
name = 'Bell'
age = 32
#argumentni pozitsiyalash
f = ('{2},{0},{1}'.format('a','b','c'))
f1 = ('{},{},{}'.format('a','b','c'))
print(f)

print( 'He is {name} and I am {age}'.format(name='Ban',age='35') )

print( 'He is {name} and I am {age}'.format(name=name,age='35') )

#f string It is only use python 3.6 greater than version
print(f'Hello world I am {name}')

#String method
h = 'i live in Uzbekistan!'
#text transform
print(h.capitalize())
print(h.upper())
print(h.lower())

#swapcase
print(h.swapcase())

#count same letter
print(h.count('a'))

print(h.startswith('i'))
print(h.startswith('I'))
print(h.endswith('!'))

k = input('Ismingizni kiriting: ')
print('Assalomu aleykum {}!'.format(k))

#kiritilgan satrning boshidan boshlab qanchadir belgisini chiqarish
print('{:.3}'.format(k))
print(k.casefold())
#len
print(len(k))
#string index
'''
0 1 2 3 4 
k i t o b 
'''
print(k[0])
print(k[2:5]) # 2 -> 5 
print(k[:5]) # 0 -> 5 
print(k[2:]) # 2 -> end

#reverse string
print(k[::-1])


#swap two word position
s = input("Satr kiriting: ")
print(s)
print(s.split())
print(' '.join(s))
print(' '.join(s.split()))
print(' '.join(s.split()[::-1]))
