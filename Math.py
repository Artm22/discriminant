import math

a = int(input(print("Введите A : ")))
b = int(input(print("Введите B : ")))
c = int(input(print("Введите C : ")))

D = (b*b) - (4*a*c)

if D > 0:
    x = (-b + math.sqrt(D)) / (2 * a)
    y = (-b - math.sqrt(D)) / (2 * a)
    print(D, x, y)
elif D == 0:
    x = - (b / (2 * a))
    print(D, x)
else:
    print(D)
    print("Корней нет")