# String
print("BroTech\nCreative\nGroup")
numbers = [1, 8, 4, 6, 7, 6, 8, 4, 6, 4, 9, 4]
numbers.sort()
numbers.reverse()
print(numbers)
# Car Game
# command = ""
# started = False
# while command != "quit":
#     command = input("-> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped...")
#     elif command == "help":
#         print(
#             """
#             start - to start the car
#             stop - to stop the car
#             quit - to quit
#             """
#         )
#     elif command =="quit":
#         break
#     else:
#         print("Sorry I don't understand! Please type \"help\" show more info!")

# for loop
# for iter in 'Hello!':
#     print(iter)
#
# for iter2 in ['Mosh', 'Krita', 'Gimp', 'Kia']:
#     print(iter2)
#
# for iter3 in range(10):
#     print(iter3)

for iter4 in range(-2, 2, 3):  # -2 dan 2 gacha 3 qadam bilan yurish!
    print(iter4)

# shopping card
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")
# generate value
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

num = [2, 5, 6, 7, 7, 8, 4]
for i in num:
    print(i * 'x')

num1 = [12, 8, 487, 8, 6, 6, 9, 56, 7, 9, 4, 49, 4, 79, 794, 64, 6]
max = num1[0]
for j in num1:
    if j > max:
        max = j
print(max)

# Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(matrix[0][1])
for row in matrix:
    for i in row:
        print(i)

num2 = [1, 5, 88, 96, 1]
# num2.append(45) #oxiriga qo`shish
num2.insert(0, 111)
print(num2)

# remove dublicate list
num3 = [1,5,4,2,7,8,9,6,4,1,5,6]
uniques = []
for num_ in num3:
    if num_ not in uniques:
        uniques.append(num_)
print(uniques)
