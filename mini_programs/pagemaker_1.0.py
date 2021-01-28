#Ikki tomonlama qilib chop qilish!
n = int(input('n = '))
print("-"*50)
print("Varaqning old tomoni: \n")
for i in range(1,n+1):
    if (i % 2 == 1):
        print(i, end=",")
        i += 1
print("\nVaraqning orqa tomoni: \n")
print("-"*50)
for i in range(1,n+1):
    if (i % 2 == 0):
        print(i, end=",")
        i += 1
print("\n")
print("-"*50)
