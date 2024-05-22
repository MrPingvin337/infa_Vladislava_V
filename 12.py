s = int(input("Введите s:"))
g = int(input("Введите g:"))
S, G = s/10, g/10
a0, a1 ,a2, a3 = (-S)*(G**2 + S**2), (G+S)**2, -(2*G+S), 1
def F(x):
    return a0 + a1*x +a2*x**2 + a3*x**3

a = float(input("Введите a: "))
b = float(input("Введите b: "))
eps = float(input("Введите Eps: "))

while abs(b - a) > eps:
    x = (a + b) / 2
    if (F(x) == 0): break
    if (F(a) * F(x) > 0):
        a = x
    else:
        b = x

print('x =',x)
print('F(x) = ', F(x))