import math
x = -2
i = 0
print("Olingan natijalar:")
while x <= 2:
    if x <= 0:
        y = float(math.cos(3*math.pow(x,3)))
    else:
        y = float(math.pow((5*x**3),1/2))
    x += 0.4
    i += 1
    print("y" + str(i) + " = ", y)