def Input_Matrix():
    f = open('input.txt', 'r')
    M = int(f.readline())
    matrix = []*M
    for i in range(M):
        matrix.append(list(map(int, f.readline().split())))
    return matrix


def Min_El(arr):
    m = 0
    for i in range(len(arr)):
            if arr[i] < m:
                m = i
    return m


def Sum_of_positive(arr):
    c = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            c += arr[i]
    return c


a = Input_Matrix()
if not a:
    print('Введена пустая матрица')
    exit()
k = int(input("Введите k:"))
if k > len(a) or k < 1:
    print('Введён неверный номер строки')
    exit()
column_of_min = Min_El(a[k-1])
sum_positive = Sum_of_positive([a[i][column_of_min] for i in range(len(a))])
print(f'Сумма положительных элементов в {column_of_min} столбце: {sum_positive}')