print("3-dars!")
#1 qatorni comment olish
''' ko`p 
qatorli 
commentlar
'''
""" ko`p 
qatorli 
commentlar
"""
a = 24 #int
print(type(a))
b = 2.1 #float
print(type(b))
c = 'John' #str
print(type(c))

'''a = float(a)
print(type(a))
'''
b = int(b)
print(type(b))


havo_issiqmi = True #bool
hova_sovuqmi = False #bool

x,y,z,t = (23,'Bell',True,2.45)
print(x)
print(z)
print(y)
print(t)

r = ('{},{},{},{}'.format(x,23,y,2.35))
print(r)
print('{},{},{},{}'.format(x,23,y,2.35))

print(c + " " + str(a) + " yoshda!")
print(f'{c} {a} yoshda!')

print('{ism} {yoshi} yoshda!'.format(ism = 'Og`abek', yoshi = x))

d = 'men Dasturlash KursIga qatnashyapmAn!'

print(d.capitalize())
print(d.upper())
print(d.lower())

print(d.startswith('M'))
print(d.endswith('!'))

print(d.count('A')+d.count('a'))

