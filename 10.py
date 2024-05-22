import random
import numpy as np
N = 3
A = np.random.randint (0, 10, (3, 3))
A = A/6
A = np.squeeze(np.asarray(A)) #Преобразуя матрицу в массив
Q, W = np.linalg.eig(A) #linalg.eig(a) - собственные значения и собственные векторы.
print("Исходный массив:")
print(A)
print("Собственные значения:")
print(Q)
print("Собственные векторы:")
for i in range (0,N):
    for j in range (0,N):
        print('%f'%W[i][j], end=' ')
    print('')