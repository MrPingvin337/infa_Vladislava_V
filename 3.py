z, x, c = int(input()), int(input()), int(input())
umax = max(z+x+c, z*x*c)
umin= min(2*z+2*x+2*c,z*x*c)
u = umax / umin
print(u)