# class Truck:
#     a = []
#     total = 0
#     def __init__ (self, cap):
#         self.cap = cap
#
#     def addTable(self, table):
#         self.a.append(table)
#         self.total += table.mass
#         if(self.total > self.cap):
#             print("Слишком много! Больше не влазит.")
#         else:
#             print("Влез стол с массой: " + str(table.mass))
#
#
#
# class Table:
#     def __init__ (self, mass):
#         self.mass = mass
#
# r1 = Truck (100)
#
# A1=Table(10)
# A2=Table(20)
# A3 = Table(20)
# A4 = Table(20)
# A5 = Table(20)
# A6 = Table(20)
#
# listOfTables = [A1, A2, A3, A4, A5, A6 ]
# for table in listOfTables:
#     r1.addTable(table)

class Book:
    def __init__(self, id, name, author, publisher, year, pages, cost, cover):
        #, author, publisher, year, pages, cost, binding):
        self.__id = id
        self.__name = name
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.cost = cost
        self.cover = cover

    def set_name(self):
         name = input('Name: ')
         self.__name = name
         return self.__name

    def set_id(self):
        id = 'aaa'
        while not id.isnumeric():
            id = input('id + : ')
        self.__id = id
        return self.__id

    def set_year(self):
        year = 'bbbb'
        while not year.isnumeric():
            year = input('year: ')
        self.year = year
        return self.year

    def get_name(self):
        return str(self.__name)

    def get_author(self):
        return str(self.author)

    def get_id(self):
        return str(self.__id)

    def get_year(self):
        return str(self.year)



print("Введите 3 книги: ")


num_1 = str(input("Введите название книги: "))
num_2 = str(input("Введите автора: "))
num_3 = str(input("Введите издателя: "))
num_4 = int(input("Введите год: "))
num_5 = int(input("Введите количество страниц: "))
num_6 = str(input("Введите переплет: "))
num_7 = int(input("Введите цену: "))
print('---------------------')

num_11 = str(input("Введите название книги: "))
num_12 = str(input("Введите автора: "))
num_13 = str(input("Введите издателя: "))
num_14 = int(input("Введите год: "))
num_15 = int(input("Введите количество страниц: "))
num_16 = str(input("Введите переплет: "))
num_17 = int(input("Введите цену: "))
print('---------------------')

num_21 = str(input("Введите название книги: "))
num_22 = str(input("Введите автора: "))
num_23 = str(input("Введите издателя: "))
num_24 = int(input("Введите год: "))
num_25 = int(input("Введите количество страниц: "))
num_26 = str(input("Введите переплет: "))
num_27 = int(input("Введите цену: "))
print('---------------------')



list_of_b = []
book_1 = Book(12, num_1, num_2, num_3, num_4, num_5, num_6, num_7)
book_2 = Book(13, num_11, num_12, num_13, num_14, num_15, num_16, num_17)
book_3 = Book(14, num_21, num_22, num_23, num_24, num_25, num_26, num_27)
list_of_b.append(book_1)
list_of_b.append(book_2)
list_of_b.append(book_3)

Book.set_id(book_1)
print(Book.get_id(book_1))
print(Book.get_id(list_of_b[0]))
if str(input('Поиск id: ')) == Book.get_id(list_of_b[0]):
    print('Такого нет')

new_list = []
search = str(input('Поиск по автору: '))
for book in list_of_b:
    if Book.get_author(book) == search:
        new_list.append(book)
for book in new_list:
    print(Book.get_name(book))

new_list_2 = []
search2 = str(input('Поиск по году: '))
for book in list_of_b:
    if Book.get_year(book) >= search2:
        new_list_2.append(book)
for book in new_list_2:
    print(Book.get_name(book))