text = "Hello Python World!"
print(text.find('o'))  # first find character print
print(text.replace('Python', 'Scala'))
print(text.find('Hello'))

print('Python' in text)

# kg to lbs
'''weight = float(input("Weight: "))
unit = input("(K)g and (L)bs: ")
#if statement
if unit.upper() == "K":
    converted = weight/0.45
    print("Weight in Lbs: " + str(converted))
elif unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))
else:
    print("Please enter same latter!")
'''
# while loops
i = 1
while i <= 10:
    print(i * '*')
    i += 1

# List
names = ["John", "Bob", "Mosh", "Sam"]
print(names[0])
print(names[-2])
names[0] = "Tony"
print(names)
print(names[:3])

# list methods
numbers = [1, 2, 3, 4, 58, 9]
# numbers.insert(0, -2)
# print(numbers)
# numbers.remove(4)
# print(numbers)
# numbers.clear()
# print(numbers)
# print(9 in numbers)
# print(len(numbers))

# for loops
for item in numbers:
    if item % 2 == 1:
        print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

#range object
num = range(10) #[0,10)
print(num)

for number in num:
    print(number)

num1 = range(5,9,1)
for number1 in num1:
    print(number1)

#tuples object (immutable)
num2 = (1,2,5,74,8,4,5,6,6)