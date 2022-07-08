#Предыдущее задание на ООП + магические методы

class Book:
  def __init__(self, id, name, author, publisher, year, pages, cost, cover):

    self.__id = id
    self.__name = name
    self.author = author
    self.publisher = publisher
    self.year = year
    self.pages = pages
    self.cost = cost
    self.cover = cover

    # методы класса

  def set_name(self):
    name = input('Name: ')
    self.__name = name
    return self.__name

  def set_id(self):  # +
    id = 'aaa'
    while not id.isnumeric():
      id = input('Изменить id: ')
    self.__id = id
    return print("Теперь id стало" + self.__id)

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

  def set_author(self, author):
    self.author = author

  def get_id(self):
    return str(self.__id)

  def get_year(self):
    return str(self.year)

  def get_publisher(self):
    return str(self.publisher)

  def set_publisher(self, publisher):
    self.publisher = publisher

  def get_cost(self):
    return str(self.cost)

  def set_cost(self, cost):
    self.cost = cost

  def get_cover(self):
    return str(self.cost)

  def set_cover(self, cover):
    self.cover = cover

  def get_pages(self):
    return str(self.pages)

  def set_pages(self, pages):
    self.pages = pages

  # статический метод
  @staticmethod
  def getBookName():
    return "Crime and Punishment"

  # метод класса
  @classmethod
  def author(cls, __name, publisher, year, pages, cost, cover):
    author = cls("Genji Monogatari", publisher, year, pages, cost, cover)
    return print("Книга" + author)

  # магические методы
  def __str__(self):
    return f'Название книги "{self.__name}", которая написана {self.author} и в ней {self.pages} страниц.'

  def __len__(self):
    return self.pages

  def __repr__(self):
    return f"Book({self.__id!r}, {self.__name!r}, {self.author!r}, {self.publisher!r}, {self.year!r}, {self.pages!r}, {self.cost!r}, {self.cover!r})"

  def __getitem__(self, author):
    return self.author

  def __mull__(self, cost):
    return cost * 0.5


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

list_of_b = list()
book_1 = Book(12, num_1, num_2, num_3, num_4, num_5, num_6, num_7)
book_2 = Book(13, num_11, num_12, num_13, num_14, num_15, num_16, num_17)
book_3 = Book(14, num_21, num_22, num_23, num_24, num_25, num_26, num_27)

book_5 = Book(15, 'Genji Monogatari', "Murasaki Shikibu", "amazon", 2010, 500, "soft", 100)

list_of_b.append(book_1)
list_of_b.append(book_2)
list_of_b.append(book_3)
list_of_b.append(book_5)

# Book.set_id(book_1)
# print(Book.get_id(book_1))
# print(Book.get_id(list_of_b[0]))
# if str(input('Поиск id: ')) == Book.get_id(list_of_b[0]):
#     print('Такого нет')

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

print("Поиск по издателю. Введите имя издательства: ")
publisher = input()
print("Информация о книгах: ")
for d in list_of_b:
  if d.publisher.lower() == publisher.lower():
    print(f"Id: {d.get_id()}")
    print(f"Название книги: {d.get_name()}")
    print(f"Автор: {d.get_author()}")
    print(f"Год: {d.get_year()}")
    print(f"Количество страниц: {d.get_pages()}")
    print(f"Стоимость: {d.get_cost()}")
    print(f"Переплет: {d.get_cover()}")
  else:
    print("Такого издетеля нет.")

print("======================")
print("Информация через __str__")
print(book_1)
print(book_2)
print(book_3)
print(book_5)
print("======================")
print("Информация через __repr__")
print(repr(list_of_b))
print("======================")
print("Информация через __len__")
print("Количество страниц в книге: " + book_1.get_name() + ": " + str(len(book_1)))
print("Количество страниц в книге: " + book_2.get_name() + ": " + str(len(book_2)))
print("Количество страниц в книге: " + book_3.get_name() + ": " + str(len(book_3)))
print("Количество страниц в книге: " + book_5.get_name() + ": " + str(len(book_5)))

print("======================")
print("Авторы книг: ")
print(book_1.__getitem__(author=num_2))
print(book_2.__getitem__(author=num_12))
print(book_3.__getitem__(author=num_22))
print(book_5.__getitem__(author='Murasaki Shikibu'))

print("======================")
print("Скидка: ")
print(book_1.__mull__(cost=num_7))
print(book_2.__mull__(cost=num_17))
print(book_3.__mull__(cost=num_27))
print(book_5.__mull__(cost=100))
