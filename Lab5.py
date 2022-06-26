# class Fib:
#     def __init__(self, max):
#         self.max = max
#
#     def __iter__(self):
#         self.a = 0
#         self.b = 0
#         self.c = 1
#         return self
#
#     def __next__(self):
#         fib = self.a
#         if fib > self.max:
#             raise StopIteration
#         fib_sum = self.a + self.b + self.c
#         self.a = self.b
#         self.b = self.c
#         self.c = fib_sum
#         # self.a, self.b, self.c = self.b, self.a + self.b, self.c + self.c
#         # fib_sum = self.a + self.b + self.c
#         return fib


# for n in Fib(1000000
#              ):
#     print(n, end=' ')

# def fib(n):
#     a, b, c = 0,0, 1
#     for i in range(n):
#         yield a
#         fib_sum = a + b + c
#         a = b
#         b = c
#         c = fib_sum
#
# print(list(fib(10))

def fib(n):
  a,b, c  = 0,0,1
  while n > 0:
    n -= 1
    yield a
    fib_sum = a + b + c
    a = b
    b = c
    c = fib_sum
    print(fib_sum)



list(fib(10))

