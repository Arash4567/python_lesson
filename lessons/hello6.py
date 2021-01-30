numbers = [5,8,7,6,1,3,1,2]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

#range object
num = range(10) #[0,10)
print(num)
for element in range(10):
    print(element,end=' ')

num1 = range(5,9,3) # +3 qadam bilan sonlarni chop qilish
for number1 in num1:
    print(number1)

#tuples (кортежи)
num = (1,2,5)
x,y,z = num
print('\n', x)

#kalitga ega qiymatlar
inson = {
    "ism": "Ahmad",
    "yosh": 19,
    "telefon": 901234567
}
print(inson['ism'])
inson['ism'] = "Ali"
print(inson['ism'])
