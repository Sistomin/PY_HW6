# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# print('Расчет арифметической прогрессии')
# n = int(input('Введите кол-во элиментов прогрессии: ')) 
# x = int(input('Введите первый элимент прогрессии:  '))
# d = int(input('Введите разность элиментов (шаг прогрессии): ')) 
# print(*range(x, x + d * n, d))

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
 
lo, hi = 3, 8
data = [randint(1, 10) for _ in range(20)]
print("Original array:", data, sep='\n')
indexes = [i for i, v in enumerate(data) if lo <= v <= hi]
print("Indexes:", indexes, sep='\n')
result = []
i = len(indexes)
while i :
    i -= 1
    result.append(data.pop(indexes[i]))
print("Remaining elements:", data, sep='\n')
print("Required elements:", result, sep='\n')