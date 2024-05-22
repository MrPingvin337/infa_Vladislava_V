import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 100)
y = (x**4) + (10*x**3) + (33*x**2) + (40*x) - 2
xmax= max(y)
xmin= min(y)
print('Минимальное значение:',xmin,'Максимальное значение:',xmax)
plt.title("График параболы")
plt.xlabel("Абсцисса - х")
plt.ylabel("Ордината - у")
plt.plot(x, y,)
plt.grid()
plt.show()
