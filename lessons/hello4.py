#4-DARS

#Bu qismda chiziqli dasturlash tuzish bilan o`tilganlarni takrorlash bo`ladi
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

# TASODIFIY KARRA JADVAL
from random import randint 

a = randint(1,9)
b = randint(1,9)

c = int(input('{} * {} = '.format(a, b)))

if c == (a * b):
    print('True!')
else: 
    print('False')


