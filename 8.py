import random
import numpy as np
N = int(input())
A = np.random.randint (0, 99, (3, 3)) #массив от 0 до 99, 3 стобца, 3 строки
B = np.random.randint (0, 99, (1, 3)) #массив от 0 до 99, 3 стобца, 1 строки
A = np.squeeze(np.asarray(A)) #Преобразуя матрицу в массив
B = np.squeeze(np.asarray(B)) #Преобразуя матрицу в массив
x = np.linalg.inv(A).dot(B) #Обратная матрица, скаляраное произведение
print('')
print('X')
for i in range (0,N):
    print('%f'%x[i],end=' ')
print('')
x1 = np.linalg.solve(A,B) # Решает систему линейных уравнений Ax = b
print('')
print('X1')
for i in range (0,N):
    print('%f'%x1[i],end=' ') # %f Подстановка числа с плавающей точкой
print('')
print('\nDet(A)=%f'%np.linalg.det(A)) # Определитель