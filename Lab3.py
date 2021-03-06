import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

def BubbleSort(A):                  # сортировка пузырьком
   for i in range(len(A)):
       for j in range(len(A)-1-i):
           if A[j] > A[j+1]:
               a = A[j]
               A[j] = A[j+1]
               A[j+1] = a

def Insert(A):  #select_sort
    for i in range(len(A)-1):
        m = i
        for j in range(i, len(A)):
            if A[j] < A[m]:
                m = j
        A[i], A[m] = A[m], A[i]


def QuickSort(A, fst, lst):         # быстрая сортировка
    if fst >= lst:
        return

    #i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой"])
x=[]
y1=[]
y2=[]
y3=[]



for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    print(A)

    B = A.copy()
    C = A.copy()
    # print(B)

    # print(A)
    # BubbleSort(A)
    # print("---")
    # print(A)


    #QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B)-1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    Insert(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Пузырьковая сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "#F933FF")
plt.plot(x, y2, "#12548c")
plt.plot(x, y3, "#12500c")
plt.show()

#Задание на рекрсию

def make_square(a, b):
    if a == b:
        squares.append(a) #добавляет в конец списка
        pass     #команда для функции, чтобы она дальше не выполнялась, если стороны одинаковые
    else:

        if a > b:
            make_square(b, a-b)
            squares.append(b)
        if b > a:
            make_square(a, b-a)
            squares.append(a)

squares = []  #список

a = "a"
b = "b"
while not a.isnumeric() or not b.isnumeric() or a == '0' or b == '0':  #проверка на целочисленность, а не стринг, чтобы не выкинуло ошибку
    print("Введите два числа (не 0):")
    a = input("1 сторона прямоугольника: ")
    b = input("2 сторона прямоугольника: ")
make_square(int(a), int(b))
print("Ребра полученных квадратов:")
print(", ".join(str(x) for x in squares))  #join - чтобы в консоли данные выводились не столбиком, а строчкой
print("Количество квадратов: " + str(len(squares))) #len считает количество элементов в списке - т.е. количество квадратов