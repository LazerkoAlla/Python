#Задание 1
#вариант 4
#найдите произведение элементов списка с нечетными номерами
#найдите наибольший элемент списка, затем удалите его и выведите новый список
from random import randint

spisok = [randint(0, 50) for i in range(20)]
sum = 0
print(spisok)
for i in spisok:
    if (i % 2) == 1:
        print(i)
        sum +=i

print(sum)

max_number = max(spisok)
print("Наибольшее число:", max_number)

spisok.remove(max_number)  # удаляем наибольшее число
print(spisok)
print('-----------')

#вариант 2
#введите одномерный целочисленные список. Найдите наибольший нечетный элемент
#найдите минимальный по модулу элемент списка

list = [randint(0, 50) for i in range(20)]
print(list)
sum1 = 0

print('Наибольший нечетный элемент:', max([i for i in list if i % 2 == 1]))
print('Минимальный по модулю элемент списка:', min([abs(i) for i in list]))
print('-----------')

#Задание 2
#Вариант 1
#В матрице найти номер строки, сумма чисел в которой максимальна

from functools import reduce
matrix = [[1, 2, 8, 9],
          [2, 2, 4, 29],
          [1, 1, 1, 100]]
matrix = [reduce(lambda a, b : a + b, i) for i in matrix] #Здесь функция определяет, какое выражение необходимо применить к итерируемому объекту.
print('Сумма строк:', matrix)
print('Номер строки, сумма чисел в которой максимальна: ', matrix.index(max(matrix))+1) #индекс строки начинается с 0, поэтому нужно добавить 1












