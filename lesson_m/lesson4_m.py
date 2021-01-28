'''
if (shart yoziladi (rost yoki yolg`on amal chiqadigan!)) : 
    shart rost bo`lsa shu qismga yoziladi
else :
    shart yolg`on qiymat qabul qilganda bajariladigan ifoda yoziladi
'''
a = 12
b = 123
# a son b sondan kattami?
# if (a > b) :
#     print('a soni b sonidan katta!')
# else :
#     print('b son a sondan katta!')

if (a > b):
    print('a son katta!')
elif (a == b):
    print('sonlar teng!')
else:
    print('b son katta!')

# biror bir butun son beriladi shu son 5 ga qoldiqsiz bo`linishini tekshiring!
c = 120
# agar son 5 ga bo`linsa 0 qoldiq qoldiq qoladi
# aksincha bo`lsa 1,2,3,4 qolqidlar qolishi mumkin
if(c % 5 == 0):
    print("bo`linadi")
else :
    print('bo`linmaydi')

# berilgan sonni juft yoki toq ekanligini aniqlang!
if(c % 2 == 0):
    print('juft')
else :
    print('toq')
# hava harorati beriladi C shkalasida havoni xusiyatini "normal", isiq, sovuq ko`rinishida chiqaring
# t - havo harorati  t<0 -> sovuq, 0<t<36 -> normal, 36<t -> isiq


#o`quvchi olgan bahoni tekshirish
baho = int(input('Olgan bahoningizni 0<baho<6 kiriting: '))
# print(baho)
if (not((0<baho)and(baho<6))): # 1,2,3,4,5
    print('O`quvchi olgan bahoni to`g`ri kiriting!')
elif ((baho == 1)or(baho == 2)):
    print('qoniqarsiz')
elif(baho == 3):
    print('qoniqarli')
elif (baho == 4):
    print('yaxshi')
else:
    print('a\'lo')

#mantiqiy operatorlar
# >
# <
# >=
# <=
# ==
# and
# or 
# not


# and uchun rostlik jadvali
'''
print(True and True)
print(True and False)
print(False and True)
print(False and False)
'''

# or uchun rostlik jadvali
'''
print(True or True)
print(True or False)
print(False or True)
print(False or False)
'''

#not uchun rostlik jadvali
'''
print(not(True))
print(not(False))
'''


#VSCode dasturini kompyuterga o`rnatish
#shu linkdan yuklab olamiz!
#https://code.visualstudio.com/  #Ctrl + mishkani chap tarafi

#Ustanovka qilish videosi
#https://www.youtube.com/watch?v=MlIzFUI1QGA


# how to install vscode in windows

# to`g`ri to`rtburchakning yuzi va perimetrini topish
# s = a * b
# P = 2 * (a + b)
a = 12
b = 56
s = a * b
print('S = ',s)
p = 2 * (a + b)
print('P = ',p)

