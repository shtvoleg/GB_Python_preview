# Задача 30:  Заполните список элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

a1 = int(input("Введите значение 1-го члена арифм. прогрессии: "))
d = int(input("Введите значение разности арифм. прогрессии: "))
n = int(input("Введите количество элементов списка: "))
my_list = [a1]
for i in range(1,n):
    my_list.append(my_list[i-1]+d)
print( *my_list)

# Пример использования:
# Введите значение 1-го члена арифм. прогрессии: 10
# Введите значение разности арифм. прогрессии: 4
# Введите количество элементов списка: 7
# [10, 14, 18, 22, 26, 30, 34]