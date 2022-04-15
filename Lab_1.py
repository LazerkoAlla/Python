#16
a = int (input("Введите целое число от 0 до 7: \n"))
if a == 1:
    print(1)
elif a == 2:
    print(2)
elif a == 3:
    print(3)
elif a == 4:
    print(4)
elif a == 5:
    print(5)
elif a == 6:
    print(6)
elif a == 7:
    print(7)

#13
b = int (input("Введите количество найденных в лесу грибов: \n"))
if b == 1:
    print("Вы нашли " + str(b) + " гриб")
elif (b in range(2, 4)) or (b in range(22, 24)):
    print("Вы нашли " + str(b) + " гриба")
elif b <= 20 or 30:
    print("Вы нашли " + str(b) + " грибов")





#6

lis = [1,2,3,4,5,6,7,8,9]
print(lis)
a = int (input("Введите целое число от 0 до 9, которое будет удалено: \n"))
val = a
if val in lis:
    lis.remove(val)
    print("Число " + str(val) + " было удалено")
print(lis)
