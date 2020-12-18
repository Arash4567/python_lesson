#My first python code 
print('Hello Python!')

''' 
long comment
'''

"""
long comment 
"""
x = 2 #int
y = 3.5 #float
name = 'Hello!' #str
name1 = "Hi!" #bool
is_best = True

x,y,name,is_cool = (20, 3.5, 'Sakid', False)


#convert another data type
x = float(x)
y = int(y)

print(x)

print(type(y))

name = 'Bell'
age = 32

print('He is ' + name + ' He is ' + str(age) + ' years old!')

#string format
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

baho = 5
if baho == 5 :
    print(baho,"-> a`lo")

a = int(input("Son kiriting: "))
if (a%2 == 1):
    print("toq son")
else: 
    print("juft son")

if (a > 0):
    print("musbat son")
elif(a < 0):
    print("manfiy son")
else:
    print("nolga teng!")

k = 1
while k<=10:
    print(k,end = ' ')
    k += 1  