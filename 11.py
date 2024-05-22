from scipy import integrate

s = int(input("Введите s:"))
g = int(input("Введите g:"))
S, G = s/10, g/10
a0, a1 ,a2, a3 = (-S)*(G**2 + S**2), (G+S)**2, -(2*G+S), 1

def F(x):
    return a0 + a1*x +a2*x**2 + a3*x**3

def INT_Count(Proc,f,a,b,eps,nmax):
    s0 = 0
    s = 1e25
    n = 4
    while(abs(s-s0)>eps) & (n<nmax):
        s0 = s
        n = 2*n
        s = Proc(f,a,b,n)
    return [s,n]

def Pr(f,a,b,n):
    h = (b - a) / n
    x = a + h / 2
    s = 0
    for i in range (n):
        s = s + f(x)
        x = x + h
    return h * s

def Tr(f,a,b,n):
    h = (b - a) / n
    x = a
    s = (f(a) + f(b)) / 2
    for i in range (1,n):
        x = x + h
        s = s + f(x)
    return h * s

def Simps(f,a,b,n):
    h = (b - a) / n
    x = a
    z = 1
    s = f(a) + f(b)
    for i in range (1,n):
        x = x + h
        s = s + (3 + z) * f(x)
        z =- z
    return h * s / 3

a = float(input("Введите a: "))
b = float(input("Введите b: "))
eps = float(input("Введите Eps: "))
nmax = int(input("Введите NMax: "))

[S,Err] = integrate.quad(F,a,b)
print('Squad = ',S,' Погрешность =' ,Err)

[S,N]=INT_Count(Pr,F,a,b,eps,nmax)
print('Sпр = ',S,' N = ',N)

[S,N]=INT_Count(Tr,F,a,b,eps,nmax)
print('Sтр = ',S,' N = ',N)

[S,N]=INT_Count(Simps,F,a,b,eps,nmax)
print('Sсимпс = ',S,' N = ',N)