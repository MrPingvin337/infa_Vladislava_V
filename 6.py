import random
spisok = random.sample(range(18), 17) # 17 случайных чисел от 0 до 17
if 0 in spisok and spisok[0] == 0:
    product1 = 0
    for number in spisok[:spisok.index(0)]:
        product1 *= number
    print("Массив:", spisok)
    print("Произведение:", product1)
    print("Сумма:", sum(spisok[spisok.index(0):]))
elif 0 in spisok:
    product1 = 1
    for number in spisok[:spisok.index(0)]:
        product1 *= number
    print("Массив:", spisok)
    print("Произведение:", product1)
    print("Сумма:", sum(spisok[spisok.index(0):]))
else:
    product2 = 1
    for number in spisok:
        product2 *= number
    print("Массив:", spisok)
    print("Произведение всех чисел:", product2)
    print("Сумма всех чисел:", sum(spisok))