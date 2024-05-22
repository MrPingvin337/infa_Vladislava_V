from math import *
t, s = int(input()), int(input())
a = cos(t) + s; b = 6*t - 3*s
rez = ((sqrt(a**2 + abs(b))) - 1) / (abs(a)+abs(b))
print('rez = ', rez) 