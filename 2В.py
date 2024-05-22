from math import *
t = int(input())
a = t; b = (2*t - 3); c = (t - 10)
if a == 0:
    x = -c / b;
    print('Является один корень: ', x)
else:
    d = (b**2) - 4*a*c
    if d <= 0:
        print('Уравнение не имеет явных корней')
    elif d > 0:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
        print('Корнями уравнения являются: ', x1, x2)